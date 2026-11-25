[← Back: Code architecture](02-architecture.md) · [README](../../README.md) · [Português (Brasil)](../pt-BR/03-desenvolvimento.md) · [Deutsch (DE)](../de-DE/03-entwicklung.md) · [Русский (RU)](../ru-RU/03-razrabotka.md) · [فارسی (ایران)](../fa-IR/03-tose-e.md) · [Next: Fidelity of the transcription →](04-fidelity.md)

# Development and quality

- Package manager: [`uv`](https://docs.astral.sh/uv/), Python 3.14 (`.python-version`).
- `make lint` — Ruff (`ruff.toml`); `make format` formats.
- Code style: Ruff formats and lints, and also enforces the blank-line rules around definitions (E30x). Ruff never inserts
  blank lines between ordinary statements, so `tools/spacing.py` applies the house style inside function bodies: one blank
  line between statements, except for runs of calls to the same function and an object followed by the calls that
  configure it (e.g. `parser = ...` then `parser.add_argument(...)`). `make format` runs it before `ruff format`;
  `make lint` runs it in `--check` mode.
- `make typecheck` — strict Mypy (`mypy.ini`).
- `make test` — Pytest (`pytest.ini`), fails below 80 % coverage.
- `make qa` runs everything; GitHub Actions (`.github/workflows/ci.yml`) does the same and
  also compiles the PDFs in all five languages.
- Python has no official LTS releases, so the latest stable version is used.
- A full render (`make image`) takes a few minutes; use `DECIMATION=4` for previews.
- Progress: `make image` and `make pdf` print per-stage progress to stderr (bars with percentage, elapsed time and ETA on
  a terminal; one line per 10 % in logs and CI). `make pdf-all` shows `[i/10]` steps with a spinner while Typst
  compiles. Add `QUIET=1` to any of them (or `--quiet` to `kiwi` / `kiwi-docs`) to silence it.
