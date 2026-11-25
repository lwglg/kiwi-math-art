from pathlib import Path

import pytest
import typst

from kiwi import docs_build
from kiwi.docs_build import LANGUAGES, human_size, output_path
from tests.test_render_progress import Recorder


def test_output_names() -> None:
    assert output_path("pt", Path("b")).name == "kiwi-pt-BR.pdf"
    assert output_path("de", Path("b")).name == "kiwi-de-DE.pdf"
    assert set(LANGUAGES) == {"en", "de", "pt", "ru", "fa"}
    assert output_path("fa", Path("b")).name == "kiwi-fa-IR.pdf"
    assert output_path("ru", Path("b")).name == "kiwi-ru-RU.pdf"


def test_unknown_language_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported"):
        output_path("fr", Path("b"))


def test_human_size() -> None:
    assert human_size(512) == "512 B"
    assert human_size(1536) == "1.5 KiB"
    assert human_size(3 * 1024 * 1024) == "3.0 MiB"


def make_project(root: Path, with_image: bool = True) -> None:
    (root / "typst").mkdir(parents=True)
    (root / "typst" / "main.typ").write_text("hello")
    (root / "build").mkdir()
    if with_image:
        from PIL import Image

        Image.new("RGB", (4, 3)).save(root / "build" / "kiwi.png")


def test_check_inputs_describes_the_sources(tmp_path: Path) -> None:
    make_project(tmp_path)
    summary = docs_build.check_inputs(tmp_path)
    assert "1 Typst modules" in summary
    assert "4x3" in summary


def test_check_inputs_explains_how_to_fix_a_missing_image(tmp_path: Path) -> None:
    make_project(tmp_path, with_image=False)
    with pytest.raises(FileNotFoundError, match="make image"):
        docs_build.check_inputs(tmp_path)


def test_missing_entry_point(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="entry point"):
        docs_build.check_inputs(tmp_path)


@pytest.fixture
def fake_typst(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> list[str]:
    calls: list[str] = []

    def fake_compile(
        entry: Path,
        output: Path,
        root: Path,
        font_paths: list[Path],
        ignore_system_fonts: bool,
        sys_inputs: dict[str, str],
    ) -> None:
        assert font_paths == [docs_build.FONTS]
        assert ignore_system_fonts
        calls.append(sys_inputs["lang"])
        output.write_bytes(b"%PDF-fake")

    monkeypatch.setattr(typst, "compile", fake_compile)
    monkeypatch.setattr(docs_build, "check_inputs", lambda root=None: "fake sources")
    return calls


def test_compile_all_builds_every_language_and_plans_stages(
    fake_typst: list[str], tmp_path: Path
) -> None:
    rec = Recorder()
    paths = docs_build.compile_all(tmp_path, rec)
    assert fake_typst == ["en", "de", "pt", "ru", "fa"]
    assert [p.name for p in paths] == [
        "kiwi-en-GB.pdf",
        "kiwi-de-DE.pdf",
        "kiwi-pt-BR.pdf",
        "kiwi-ru-RU.pdf",
        "kiwi-fa-IR.pdf",
    ]
    assert rec.planned == 10
    assert len(rec.stages) == 10


def test_main_single_language_and_quiet(
    fake_typst: list[str], tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert docs_build.main(["-l", "pt", "-o", str(tmp_path), "-q"]) == 0
    out = capsys.readouterr()
    assert fake_typst == ["pt"]
    assert "kiwi-pt-BR.pdf" in out.out
    assert out.err == ""


def test_main_all_reports_progress(fake_typst: list[str], tmp_path: Path) -> None:
    rec = Recorder()
    assert docs_build.main(["-l", "all", "-o", str(tmp_path)], reporter=rec) == 0
    assert fake_typst == ["en", "de", "pt", "ru", "fa"]
    assert rec.messages[0].startswith("kiwi-docs: building en-GB, de-DE, pt-BR, ru-RU, fa-IR")
    assert rec.messages[-1].startswith("done: 5 PDF(s)")
