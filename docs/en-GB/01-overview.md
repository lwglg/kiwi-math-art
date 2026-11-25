[README](../../README.md) · [Português (Brasil)](../pt-BR/01-visao-geral.md) · [Deutsch (DE)](../de-DE/01-uebersicht.md) · [Русский (RU)](../ru-RU/01-obzor.md) · [فارسی (ایران)](../fa-IR/01-nemaye-koli.md) · [Next: Code architecture →](02-architecture.md)

# Overview

The 2000 × 1060 image is defined by three functions $H_0, H_1, H_2$ of two real variables.
The chain of computation is:

`(m, n) → (x, y) → (δᵣ, Tᵣ, Uᵣ, Jᵣ) → (Z, Lₛ) → (A, B, E, u, v, Kₛ) → Hₛ → F → rgb`

- `x = (m − 1300)/540`, `y = (531 − n)/540`
- Smooth switches `σₖ(u) = exp(−exp(−k u))` and `εₖ(u) = exp(−exp(k u))` replace `if`.
- 100 hair strokes `Jᵣ` painted in order; 40 bokeh patches `Kₛ` in the background.
- `A` is the beak, `B` the legs; the eye is cut out of the painted feathers only.

The PDFs (`make pdf LANG_CODE=en`) present this chain in textbook style, crediting
[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh) (original artwork) and Guilherme Lima Gonçalves (augmented project).
