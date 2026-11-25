[README](../../README.pt-BR.md) · [English (UK)](../en-GB/01-overview.md) · [Deutsch (DE)](../de-DE/01-uebersicht.md) · [Русский (RU)](../ru-RU/01-obzor.md) · [فارسی (ایران)](../fa-IR/01-nemaye-koli.md) · [Próximo: Arquitetura do código →](02-arquitetura.md)

# Visão geral

A imagem de 2000 × 1060 pixels é definida por três funções $H_0, H_1, H_2$ de duas variáveis reais.
A cadeia de cálculo é:

`(m, n) → (x, y) → (δᵣ, Tᵣ, Uᵣ, Jᵣ) → (Z, Lₛ) → (A, B, E, u, v, Kₛ) → Hₛ → F → rgb`

- `x = (m − 1300)/540`, `y = (531 − n)/540`
- Chaves suaves `σₖ(u) = exp(−exp(−k u))` e `εₖ(u) = exp(−exp(k u))` substituem `if`.
- 100 traços de pelo `Jᵣ` pintados em ordem; 40 manchas de bokeh `Kₛ` no fundo.
- `A` é o bico, `B` as patas; o olho é recortado apenas das penas pintadas.

Os PDFs (`make pdf LANG_CODE=pt`) apresentam essa cadeia em formato de livro-texto, com autoria
de [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh) (obra original) e Guilherme Lima Gonçalves (projeto ampliado).
