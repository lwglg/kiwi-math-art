"""Command line entry point: ``kiwi --output build/kiwi.png [-d 4] [-q]``."""

from __future__ import annotations

import argparse
import time
from collections.abc import Sequence
from pathlib import Path

from kiwi.canvas import Canvas
from kiwi.imageio import save_png
from kiwi.progress import ConsoleReporter, NullReporter, Reporter, format_duration
from kiwi.render import N_STAGES, render_rgb


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kiwi", description="Render the formula kiwi.")
    parser.add_argument("-o", "--output", type=Path, default=Path("build/kiwi.png"))
    parser.add_argument(
        "-d",
        "--decimation",
        type=int,
        default=1,
        help="render every d-th pixel (1 = full 2000x1060 image)",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="no progress output")

    return parser


def main(argv: Sequence[str] | None = None, reporter: Reporter | None = None) -> int:
    args = build_parser().parse_args(argv)

    rep: Reporter = reporter or (NullReporter() if args.quiet else ConsoleReporter())

    canvas = Canvas(decimation=args.decimation)

    started = time.perf_counter()

    rep.message(
        f"kiwi: rendering {canvas.out_width}x{canvas.out_height} "
        f"(decimation {args.decimation}) -> {args.output}"
    )

    rep.plan(N_STAGES + 1)

    pixels = render_rgb(canvas, rep)

    rep.stage("Saving PNG", 1)

    path = save_png(pixels, args.output)

    rep.advance()

    rep.end(f"{path.stat().st_size / 1024:,.0f} KiB")

    rep.message(
        f"wrote {path} ({pixels.shape[1]}x{pixels.shape[0]}) "
        f"in {format_duration(time.perf_counter() - started)}"
    )

    return 0
