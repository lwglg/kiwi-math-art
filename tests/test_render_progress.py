from pathlib import Path

import pytest

from kiwi.canvas import Canvas
from kiwi.cli import main
from kiwi.render import N_STAGES, render_rgb


class Recorder:
    def __init__(self) -> None:
        self.stages: list[tuple[str, int | None]] = []
        self.advances = 0
        self.messages: list[str] = []
        self.planned = 0

    def plan(self, stages: int) -> None:
        self.planned = stages

    def stage(self, label: str, total: int | None = None) -> None:
        self.stages.append((label, total))

    def advance(self, n: int = 1) -> None:
        self.advances += n

    def end(self, detail: str = "") -> None:
        return None

    def message(self, text: str) -> None:
        self.messages.append(text)


def test_render_reports_every_stage() -> None:
    rec = Recorder()
    render_rgb(Canvas(decimation=80), rec)
    assert len(rec.stages) == N_STAGES
    assert [t for _, t in rec.stages] == [1, 100, 40, 3, 3]
    assert rec.advances == 1 + 100 + 40 + 3 + 3


def test_cli_reports_and_plans_one_extra_stage(tmp_path: Path) -> None:
    rec = Recorder()
    assert main(["-o", str(tmp_path / "k.png"), "-d", "80"], reporter=rec) == 0
    assert rec.planned == N_STAGES + 1
    assert rec.stages[-1][0] == "Saving PNG"
    assert rec.messages[0].startswith("kiwi: rendering")
    assert rec.messages[-1].startswith("wrote")


def test_quiet_flag_prints_nothing(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-q", "-o", str(tmp_path / "k.png"), "-d", "80"]) == 0
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
