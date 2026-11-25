from pathlib import Path

import pytest
from tools.spacing import format_source, main, missing_blank_lines, python_files


BEFORE = """\
def main(argv: Sequence[str] | None = None, reporter: Reporter | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kiwi-docs")
    parser.add_argument("-l", "--lang", choices=[*sorted(LANGUAGES), "all"], required=True)
    parser.add_argument("-o", "--out-dir", type=Path, default=None)
    parser.add_argument("-q", "--quiet", action="store_true", help="no progress output")
    args = parser.parse_args(argv)
    rep: Reporter = reporter or (NullReporter() if args.quiet else ConsoleReporter())
    started = time.perf_counter()
    langs = list(LANGUAGES) if args.lang == "all" else [args.lang]
    rep.message(f"kiwi-docs: building {', '.join(LANGUAGES[x] for x in langs)}")
    if args.lang == "all":
        paths = compile_all(args.out_dir, rep)
    else:
        rep.plan(STAGES_PER_LANGUAGE)
        paths = [compile_pdf(args.lang, args.out_dir, rep)]
    elapsed = format_duration(time.perf_counter() - started)
    for path in paths:
        print(f"wrote {path}")
    rep.message(f"done: {len(paths)} PDF(s) in {elapsed}")
    return 0
"""

AFTER = """\
def main(argv: Sequence[str] | None = None, reporter: Reporter | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kiwi-docs")
    parser.add_argument("-l", "--lang", choices=[*sorted(LANGUAGES), "all"], required=True)
    parser.add_argument("-o", "--out-dir", type=Path, default=None)
    parser.add_argument("-q", "--quiet", action="store_true", help="no progress output")

    args = parser.parse_args(argv)

    rep: Reporter = reporter or (NullReporter() if args.quiet else ConsoleReporter())

    started = time.perf_counter()

    langs = list(LANGUAGES) if args.lang == "all" else [args.lang]

    rep.message(f"kiwi-docs: building {', '.join(LANGUAGES[x] for x in langs)}")

    if args.lang == "all":
        paths = compile_all(args.out_dir, rep)
    else:
        rep.plan(STAGES_PER_LANGUAGE)
        paths = [compile_pdf(args.lang, args.out_dir, rep)]

    elapsed = format_duration(time.perf_counter() - started)

    for path in paths:
        print(f"wrote {path}")

    rep.message(f"done: {len(paths)} PDF(s) in {elapsed}")

    return 0
"""


def test_the_reference_example_is_reproduced_exactly() -> None:
    assert format_source(BEFORE) == AFTER


def test_formatting_is_idempotent() -> None:
    assert format_source(AFTER) == AFTER
    assert missing_blank_lines(AFTER) == []


def test_docstring_and_first_statement_stay_tight() -> None:
    source = 'def f():\n    """Doc."""\n    a = 1\n    b = 2\n'
    assert format_source(source) == 'def f():\n    """Doc."""\n    a = 1\n\n    b = 2\n'


def test_comments_travel_with_the_following_statement() -> None:
    source = "def f():\n    a = 1\n    # explain b\n    b = 2\n"
    assert format_source(source) == "def f():\n    a = 1\n\n    # explain b\n    b = 2\n"


def test_nested_blocks_and_module_level_are_untouched() -> None:
    source = "A = 1\nB = 2\n\n\ndef f():\n    if A:\n        x = 1\n        y = 2\n"
    assert format_source(source) == source


def test_nested_functions_get_their_own_spacing() -> None:
    source = "def outer():\n    def inner():\n        a = 1\n        b = 2\n    return inner\n"
    assert "        a = 1\n\n        b = 2\n" in format_source(source)


def test_decorated_definitions_keep_decorators_attached() -> None:
    source = "def f():\n    x = 1\n    @deco\n    def g():\n        pass\n"
    assert "    x = 1\n\n    @deco\n    def g" in format_source(source)


def test_object_stays_tight_with_its_configuration_calls() -> None:
    source = "def f():\n    p = make()\n    p.add(1)\n    q = p.build()\n"
    assert format_source(source) == "def f():\n    p = make()\n    p.add(1)\n\n    q = p.build()\n"


def test_different_calls_are_not_grouped() -> None:
    source = "def f():\n    a.one()\n    a.two()\n"
    assert format_source(source) == "def f():\n    a.one()\n\n    a.two()\n"


def test_cli_check_and_rewrite(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    target = tmp_path / "m.py"
    target.write_text("def f():\n    a = 1\n    b = 2\n")
    assert main(["--check", str(tmp_path)]) == 1
    assert "1 missing blank line(s)" in capsys.readouterr().out
    assert target.read_text() == "def f():\n    a = 1\n    b = 2\n"

    assert main([str(tmp_path)]) == 0
    assert target.read_text() == "def f():\n    a = 1\n\n    b = 2\n"
    assert main(["--check", str(tmp_path)]) == 0


def test_python_files_skips_tool_directories(tmp_path: Path) -> None:
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "x.py").write_text("")
    (tmp_path / "ok.py").write_text("")
    assert [p.name for p in python_files([tmp_path])] == ["ok.py"]


def test_module_runs_from_the_command_line(tmp_path: Path) -> None:
    import subprocess
    import sys

    target = tmp_path / "m.py"
    target.write_text("def f():\n    a = 1\n    b = 2\n")
    root = Path(__file__).resolve().parents[1]
    command = [sys.executable, "-m", "tools.spacing", "--check", str(target)]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert result.returncode == 1
    assert "missing blank line" in result.stdout
