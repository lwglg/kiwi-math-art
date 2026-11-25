[← Back: Overview](01-overview.md) · [README](../../README.md) · [Português (Brasil)](../pt-BR/02-arquitetura.md) · [Deutsch (DE)](../de-DE/02-architektur.md) · [Русский (RU)](../ru-RU/02-arhitektura.md) · [فارسی (ایران)](../fa-IR/02-memari.md) · [Next: Development and quality →](03-development.md)

# Code architecture

| Module (`src/kiwi/`) | Responsibility | PDF section |
|---|---|---|
| `numerics.py` | smooth switches `step`/`cutoff`/`dexp` | 2 |
| `canvas.py` | pixel → plane | 1 |
| `transfer.py` | function `F` (real → byte) | 1 |
| `feathers.py` | `δᵣ`, `Tᵣ`, `Uᵣ`, `Jᵣ` | 3 |
| `shading.py` | `Z`, `Lₛ` | 3 |
| `masks.py` | beak `A`, legs `B`, levels `u`/`v`, eye `E` | 4 |
| `background.py` | blurred background `Kₛ` | 5 |
| `palette.py` | assembly of `Hₛ` | 6 |
| `progress.py` | progress reporting | — |
| `render.py`, `imageio.py`, `cli.py` | execution and output | — |
| `docs_build.py` | compiles the Typst sources | — |
| `tools/spacing.py` (outside the package) | statement spacing for `make format` / `make lint` | — |

Typst (`typst/`): `main.typ` (entry point), `lib/` (theme, authorship, notation),
`sections/` (one section per file, maths only) and `lang/` (per-language text).
To add a PDF language, create `lang/<code>.typ` and register it in `main.typ` and `docs_build.py`.
Right-to-left languages (Persian) need no extra layout work: Typst derives the direction from `lang`, and the dictionary only sets an Arabic-script `font` (plus `size` and `leading`). `typst/fonts/` holds the bundled Vazirmatn font (SIL OFL); builds ignore system fonts, so PDFs are reproducible.

Markdown documentation lives in `docs/<language>/`; `README.md` is the default (en-GB) entry point.
