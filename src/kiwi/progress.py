"""Progress reporting shared by the image renderer and the PDF builder.

A :class:`Reporter` is told about *stages* (``stage``), their progress
(``advance``) and their end (``end``). :class:`NullReporter` ignores everything
(library and test default); :class:`ConsoleReporter` writes to ``stderr``:

* on a terminal: a live bar with percentage, elapsed time and ETA, or a spinner
  with elapsed time for stages of unknown length;
* otherwise (CI, pipes): plain lines, one per 10 % step, so logs stay short.
"""

from __future__ import annotations

import sys
import threading
import time
from collections.abc import Callable
from typing import Protocol, TextIO


SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"


def format_duration(seconds: float) -> str:
    """``75.2`` -> ``1:15``; ``3700`` -> ``1:01:40``."""
    total = int(seconds + 0.5)

    minutes, secs = divmod(total, 60)

    hours, minutes = divmod(minutes, 60)

    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


class Reporter(Protocol):
    """What the pipelines need to report progress."""

    def plan(self, stages: int) -> None: ...

    def stage(self, label: str, total: int | None = None) -> None: ...

    def advance(self, n: int = 1) -> None: ...

    def end(self, detail: str = "") -> None: ...

    def message(self, text: str) -> None: ...


class NullReporter:
    """Reporter that does nothing."""

    def plan(self, stages: int) -> None:
        return None

    def stage(self, label: str, total: int | None = None) -> None:
        return None

    def advance(self, n: int = 1) -> None:
        return None

    def end(self, detail: str = "") -> None:
        return None

    def message(self, text: str) -> None:
        return None


class ConsoleReporter:
    """Human-friendly reporter writing to a text stream (``stderr`` by default)."""

    def __init__(
        self,
        stream: TextIO | None = None,
        interactive: bool | None = None,
        clock: Callable[[], float] = time.perf_counter,
        bar_width: int = 24,
        spin_interval: float = 0.1,
    ) -> None:
        self.stream: TextIO = stream if stream is not None else sys.stderr

        self.interactive = self.stream.isatty() if interactive is None else interactive

        self._clock = clock

        self._bar_width = bar_width

        self._spin_interval = spin_interval

        self._planned = 0

        self._index = 0

        self._label = ""

        self._total: int | None = None

        self._done = 0

        self._started = 0.0

        self._last_draw = 0.0

        self._last_decile = -1

        self._open = False

        self._stop = threading.Event()

        self._thread: threading.Thread | None = None

        self._lock = threading.Lock()

    # -- public API -----------------------------------------------------
    def plan(self, stages: int) -> None:
        self._planned = stages

    def stage(self, label: str, total: int | None = None) -> None:
        if self._open:
            self.end()

        self._index += 1

        self._label, self._total, self._done = label, total, 0

        self._started = self._last_draw = self._clock()

        self._last_decile = -1

        self._open = True

        if total is None:
            self._start_spinner()
        else:
            self._draw(force=True)

    def advance(self, n: int = 1) -> None:
        if not self._open:
            return

        self._done += n

        self._draw(force=self._total is not None and self._done >= self._total)

    def end(self, detail: str = "") -> None:
        if not self._open:
            return

        self._stop_spinner()

        elapsed = format_duration(self._clock() - self._started)

        extra = f"  {detail}" if detail else ""

        self._write(f"{self._prefix()} {self._label:<30} ✓ {elapsed}{extra}", final=True)

        self._open = False

    def message(self, text: str) -> None:
        self._write(text, final=True)

    # -- internals ------------------------------------------------------
    def _prefix(self) -> str:
        return f"[{self._index}/{self._planned}]" if self._planned else f"[{self._index}]"

    def _bar_line(self) -> str:
        assert self._total is not None

        frac = min(self._done / self._total, 1.0) if self._total else 1.0

        filled = int(frac * self._bar_width)

        bar = "█" * filled + "░" * (self._bar_width - filled)

        elapsed = self._clock() - self._started

        eta = elapsed / frac * (1 - frac) if frac > 0 else 0.0

        return (
            f"{self._prefix()} {self._label:<30} {bar} {self._done}/{self._total} "
            f"{int(frac * 100):3d}%  {format_duration(elapsed)}  ETA {format_duration(eta)}"
        )

    def _draw(self, force: bool) -> None:
        if self._total is None:
            return

        now = self._clock()

        if self.interactive:
            if force or now - self._last_draw >= 0.05:
                self._last_draw = now
                self._write(self._bar_line(), final=False)
            return

        if self._total < 10:
            return

        decile = int(min(self._done / self._total, 1.0) * 10)

        if decile > self._last_decile:
            self._last_decile = decile
            self._write(self._bar_line(), final=True)

    def _write(self, text: str, final: bool) -> None:
        with self._lock:
            if self.interactive:
                self.stream.write("\r\033[K" + text + ("\n" if final else ""))
            else:
                self.stream.write(text + "\n")
            self.stream.flush()

    def _start_spinner(self) -> None:
        if not self.interactive:
            self._write(f"{self._prefix()} {self._label} …", final=True)
            return

        self._stop.clear()

        self._thread = threading.Thread(target=self._spin, daemon=True)

        self._thread.start()

    def _spin(self) -> None:
        tick = 0

        while not self._stop.is_set():
            elapsed = format_duration(self._clock() - self._started)
            frame = SPINNER[tick % len(SPINNER)]
            self._write(f"{self._prefix()} {frame} {self._label} … {elapsed}", final=False)
            tick += 1
            self._stop.wait(self._spin_interval)

    def _stop_spinner(self) -> None:
        if self._thread is not None:
            self._stop.set()
            self._thread.join()
            self._thread = None
