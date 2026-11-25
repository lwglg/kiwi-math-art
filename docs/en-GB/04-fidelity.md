[← Back: Development and quality](03-development.md) · [README](../../README.md) · [Português (Brasil)](../pt-BR/04-fidelidade.md) · [Deutsch (DE)](../de-DE/04-treue.md) · [Русский (RU)](../ru-RU/04-tochnost.md) · [فارسی (ایران)](../fa-IR/04-dorosti.md)

# Fidelity of the transcription

All formulas were transcribed from the enlarged (1600 × 1600) image of the original artwork; the Python code
implements exactly what the PDFs print. A first reading from an 800 × 800 image contained several errors
(for instance `cos(107·Tᵣ + 5r)`, where the correct term is `cos(10·Tᵣ + 5r)`) and was replaced.

| Element | Reading |
|---|---|
| Pixel map, `F`, `A`, `B`, `u`, `v`, `E`, `Lₛ`, `Tᵣ`, `Uᵣ`, `Kₛ` | Clear |
| Constant `2/58` in `θᵣ` | Low legibility |
| Offset `y − 8` in `Pᵣ`, `Qᵣ` (could be `y − 9`) | Low legibility |
| Reach `λᵣ = 29/88 (1 + √(r/100)) − 3/2 \|(r−50)/45\|³` | Grouping chosen so that the body outline closes |

If you have the original formula text, check these three points in `feathers.py` and `background.py`.
