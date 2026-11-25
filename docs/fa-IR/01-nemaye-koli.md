<div dir="rtl" lang="fa">

[README](../../README.fa-IR.md) · [English (UK)](../en-GB/01-overview.md) · [Português (Brasil)](../pt-BR/01-visao-geral.md) · [Deutsch (DE)](../de-DE/01-uebersicht.md) · [Русский (RU)](../ru-RU/01-obzor.md) · [بعدی: معماری کد →](02-memari.md)

# نمای کلی

تصویر $2000 times 1060$ پیکسلی با سه تابع $H_0, H_1, H_2$ از دو متغیر حقیقی تعریف می‌شود.
زنجیره‌ی محاسبه چنین است:

`(m, n) → (x, y) → (δᵣ, Tᵣ, Uᵣ, Jᵣ) → (Z, Lₛ) → (A, B, E, u, v, Kₛ) → Hₛ → F → rgb`

- `x = (m − 1300)/540` و `y = (531 − n)/540`
- کلیدهای هموار `σₖ(u) = exp(−exp(−k u))` و `εₖ(u) = exp(−exp(k u))` جای `if` را می‌گیرند.
- 100 تار مو `Jᵣ` که به‌ترتیب رنگ می‌شوند؛ 40 لکه‌ی بوکه `Kₛ` در پس‌زمینه.
- `A` نوک و `B` پاهاست؛ چشم فقط از پرهای رنگ‌شده بریده می‌شود.

فایل‌های PDF (`make pdf LANG_CODE=fa`) این زنجیره را به سبک کتاب درسی ارائه می‌کنند و از
[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh) (اثر اصلی) و Guilherme Lima Gonçalves (پروژه‌ی گسترش‌یافته) نام می‌برند.

</div>
