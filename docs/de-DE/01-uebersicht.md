[README](../../README.de-DE.md) · [English (UK)](../en-GB/01-overview.md) · [Português (Brasil)](../pt-BR/01-visao-geral.md) · [Русский (RU)](../ru-RU/01-obzor.md) · [فارسی (ایران)](../fa-IR/01-nemaye-koli.md) · [Weiter: Code-Architektur →](02-architektur.md)

# Überblick

Das Bild mit 2000 × 1060 Pixeln wird durch drei Funktionen $H_0, H_1, H_2$ zweier reeller Variablen festgelegt.
Die Rechenkette lautet:

`(m, n) → (x, y) → (δᵣ, Tᵣ, Uᵣ, Jᵣ) → (Z, Lₛ) → (A, B, E, u, v, Kₛ) → Hₛ → F → rgb`

- `x = (m − 1300)/540`, `y = (531 − n)/540`
- Glatte Schalter `σₖ(u) = exp(−exp(−k u))` und `εₖ(u) = exp(−exp(k u))` ersetzen `if`.
- 100 Haarstriche `Jᵣ`, der Reihe nach gemalt; 40 Bokeh-Flecken `Kₛ` im Hintergrund.
- `A` ist der Schnabel, `B` sind die Beine; das Auge wird nur aus den gemalten Federn ausgeschnitten.

Die PDFs (`make pdf LANG_CODE=de`) stellen diese Kette lehrbuchartig dar und nennen
[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh) (Originalwerk) und Guilherme Lima Gonçalves (erweitertes Projekt).
