[README](../../README.ru-RU.md) · [English (UK)](../en-GB/01-overview.md) · [Português (Brasil)](../pt-BR/01-visao-geral.md) · [Deutsch (DE)](../de-DE/01-uebersicht.md) · [فارسی (ایران)](../fa-IR/01-nemaye-koli.md) · [Далее: Архитектура кода →](02-arhitektura.md)

# Обзор

Изображение размером 2000 × 1060 пикселей задаётся тремя функциями $H_0, H_1, H_2$ двух вещественных переменных.
Цепочка вычислений такова:

`(m, n) → (x, y) → (δᵣ, Tᵣ, Uᵣ, Jᵣ) → (Z, Lₛ) → (A, B, E, u, v, Kₛ) → Hₛ → F → rgb`

- `x = (m − 1300)/540`, `y = (531 − n)/540`
- Гладкие переключатели `σₖ(u) = exp(−exp(−k u))` и `εₖ(u) = exp(−exp(k u))` заменяют `if`.
- 100 штрихов шерсти `Jᵣ`, рисуемых по порядку; 40 пятен боке `Kₛ` на фоне.
- `A` — клюв, `B` — лапы; глаз вырезается только из нарисованных перьев.

PDF-файлы (`make pdf LANG_CODE=ru`) излагают эту цепочку в учебном стиле и указывают
[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh) (оригинальная работа) и Guilherme Lima Gonçalves (расширенный проект).
