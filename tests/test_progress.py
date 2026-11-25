import io

from kiwi.progress import ConsoleReporter, NullReporter, format_duration


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now


def test_format_duration() -> None:
    assert format_duration(0) == "0:00"
    assert format_duration(75.2) == "1:15"
    assert format_duration(3700) == "1:01:40"


def test_null_reporter_accepts_everything() -> None:
    rep = NullReporter()
    rep.plan(2)
    rep.stage("x", 3)
    rep.advance()
    rep.message("hello")
    rep.end("done")


def test_log_mode_prints_one_line_per_decile() -> None:
    out, clock = io.StringIO(), FakeClock()
    rep = ConsoleReporter(stream=out, interactive=False, clock=clock)
    rep.plan(1)
    rep.stage("Feathers", 20)
    for _ in range(20):
        clock.now += 1.0
        rep.advance()
    rep.end("ok")
    lines = out.getvalue().splitlines()
    assert lines[0].startswith("[1/1] Feathers")
    assert "  0%" in lines[0]
    assert "100%" in lines[-2]
    assert "✓ 0:20  ok" in lines[-1]
    assert len(lines) == 12  # 0 %, ten steps, final line


def test_small_stages_print_only_the_final_line() -> None:
    out = io.StringIO()
    rep = ConsoleReporter(stream=out, interactive=False, clock=FakeClock())
    rep.stage("Tiny", 3)
    rep.advance(3)
    rep.end()
    assert out.getvalue().count("\n") == 1
    assert "[1] Tiny" in out.getvalue()


def test_eta_is_estimated_from_elapsed_time() -> None:
    out, clock = io.StringIO(), FakeClock()
    rep = ConsoleReporter(stream=out, interactive=False, clock=clock)
    rep.stage("Work", 10)
    clock.now = 10.0
    rep.advance(5)
    assert "ETA 0:10" in out.getvalue().splitlines()[-1]


def test_a_new_stage_closes_the_previous_one() -> None:
    out = io.StringIO()
    rep = ConsoleReporter(stream=out, interactive=False, clock=FakeClock())
    rep.stage("A", 2)
    rep.stage("B", 2)
    assert "A" in out.getvalue()
    assert "✓" in out.getvalue()


def test_interactive_mode_redraws_in_place() -> None:
    out, clock = io.StringIO(), FakeClock()
    rep = ConsoleReporter(stream=out, interactive=True, clock=clock)
    rep.stage("Bar", 4)
    for _ in range(4):
        clock.now += 1.0
        rep.advance()
    rep.end()
    assert "\r\033[K" in out.getvalue()
    assert out.getvalue().endswith("\n")


def test_spinner_runs_for_indeterminate_stages() -> None:
    out = io.StringIO()
    rep = ConsoleReporter(stream=out, interactive=True, spin_interval=0.01)
    rep.stage("Compiling")
    import time

    time.sleep(0.05)
    rep.end("pdf")
    assert "Compiling" in out.getvalue()
    assert "✓" in out.getvalue()


def test_indeterminate_stage_in_log_mode_prints_start_and_end() -> None:
    out = io.StringIO()
    rep = ConsoleReporter(stream=out, interactive=False, clock=FakeClock())
    rep.stage("Compiling")
    rep.end()
    assert out.getvalue().count("\n") == 2


def test_calls_without_an_open_stage_are_ignored() -> None:
    out = io.StringIO()
    rep = ConsoleReporter(stream=out, interactive=False, clock=FakeClock())
    rep.advance()
    rep.end()
    assert out.getvalue() == ""
