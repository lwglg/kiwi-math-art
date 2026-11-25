"""Statement spacing for function bodies, the companion of ``ruff format``.

Ruff keeps the blank lines you write but never adds them between ordinary
statements, so this tool applies the project's house style. Inside every
function body, each statement is separated from the previous one by a blank
line, except that

* the first statement (and a docstring with the statement after it) stays tight;
* consecutive expression statements calling the same function stay together
  (a run of ``parser.add_argument(...)`` calls reads as one block);
* an assignment ``name = ...`` stays tight with the ``name.method(...)`` call
  statements that configure the new object right after it;
* comments directly above a statement travel with it.

Only the top level of a function body is spaced; nested blocks are left as
written. Usage: ``python -m tools.spacing [--check] PATH...``.
"""

from __future__ import annotations

import argparse
import ast
from collections.abc import Iterable, Iterator, Sequence
from pathlib import Path


SKIPPED_DIRS = {".venv", "build", "__pycache__", ".git", ".mypy_cache", ".ruff_cache"}


def _is_docstring(stmt: ast.stmt) -> bool:
    return (
        isinstance(stmt, ast.Expr)
        and isinstance(stmt.value, ast.Constant)
        and isinstance(stmt.value.value, str)
    )


def _call_key(stmt: ast.stmt) -> str | None:
    """Identity of the called function for ``f(...)`` expression statements."""
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        return ast.dump(stmt.value.func)

    return None


def _assigned_name(stmt: ast.stmt) -> str | None:
    """``x`` for ``x = ...`` and ``x: T = ...``; ``None`` for anything else."""
    if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
        target: ast.expr = stmt.targets[0]
    elif isinstance(stmt, ast.AnnAssign):
        target = stmt.target
    else:
        return None

    return target.id if isinstance(target, ast.Name) else None


def _method_receiver(stmt: ast.stmt) -> str | None:
    """``x`` for an expression statement ``x.method(...)``."""
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        func = stmt.value.func
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            return func.value.id

    return None


def _grouped(previous: ast.stmt, current: ast.stmt) -> bool:
    key = _call_key(previous)

    if key is not None and key == _call_key(current):
        return True

    name = _assigned_name(previous)

    return name is not None and name == _method_receiver(current)


def _start_line(stmt: ast.stmt, lines: Sequence[str], floor: int) -> int:
    """First line of ``stmt`` (1-based), including decorators and leading comments."""
    decorators: list[ast.expr] = getattr(stmt, "decorator_list", [])

    first: int = min([stmt.lineno, *(d.lineno for d in decorators)])

    while first - 1 > floor and lines[first - 2].lstrip().startswith("#"):
        first -= 1

    return first


def _function_bodies(tree: ast.AST) -> Iterator[list[ast.stmt]]:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            yield node.body


def missing_blank_lines(source: str) -> list[int]:
    """1-based line numbers before which a blank line must be inserted."""
    lines = source.splitlines()

    insertions: set[int] = set()

    for body in _function_bodies(ast.parse(source)):
        for index in range(1, len(body)):
            previous, current = body[index - 1], body[index]
            if (index == 1 and _is_docstring(previous)) or _grouped(previous, current):
                continue
            assert previous.end_lineno is not None
            start = _start_line(current, lines, previous.end_lineno)
            if lines[start - 2].strip():
                insertions.add(start)

    return sorted(insertions)


def format_source(source: str) -> str:
    """Return ``source`` with the house spacing applied (idempotent)."""
    insertions = set(missing_blank_lines(source))

    if not insertions:
        return source

    out: list[str] = []

    for number, line in enumerate(source.splitlines(keepends=True), start=1):
        if number in insertions:
            out.append("\n")
        out.append(line)

    return "".join(out)


def python_files(paths: Iterable[Path]) -> Iterator[Path]:
    for path in paths:
        if path.is_dir():
            for found in sorted(path.rglob("*.py")):
                if not SKIPPED_DIRS.intersection(found.parts):
                    yield found
        else:
            yield path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="spacing", description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--check", action="store_true", help="report instead of rewriting")

    args = parser.parse_args(argv)

    failures = 0

    for path in python_files(args.paths):
        source = path.read_text(encoding="utf-8")
        missing = missing_blank_lines(source)
        if not missing:
            continue

        if args.check:
            failures += 1
            print(f"{path}: {len(missing)} missing blank line(s), first at line {missing[0]}")
        else:
            path.write_text(format_source(source), encoding="utf-8")
            print(f"spaced {path} (+{len(missing)})")

    return 1 if failures else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
