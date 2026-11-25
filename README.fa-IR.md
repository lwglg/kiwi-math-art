<div dir="rtl" lang="fa">

# kiwi-math-art

[🇬🇧 English (UK)](README.md) · [🇧🇷 Português (Brasil)](README.pt-BR.md) · [🇩🇪 Deutsch (DE)](README.de-DE.md) · [🇷🇺 Русский (RU)](README.ru-RU.md) · **🇮🇷 فارسی (ایران)**

مستندات ریاضی (Typst، به en-GB، de-DE، pt-BR، ru-RU و fa-IR) و پیاده‌سازی پایتونِ یک کیوی که تنها با فرمول‌ها
کشیده شده است، بر پایه‌ی اثر [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh).

اثر اصلی: **[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)** — [LinkedIn](https://www.linkedin.com/in/hamidnaderiyeganeh) · [X](https://x.com/naderi_yeganeh) · [YouTube](https://www.youtube.com/@naderiyeganeh)

پروژه‌ی گسترش‌یافته از **Guilherme Lima Gonçalves** — [LinkedIn](https://linkedin.com/in/guligon90) · [GitHub](https://github.com/lwglg) · [صفحه‌ی شخصی](https://lwglg.github.io/portfolio-spa)

> فرمول‌ها از تصویر بزرگ‌شده رونویسی شده‌اند؛ چند ثابت کوچک کم‌خوانا هستند. ببینید [درستی رونویسی](docs/fa-IR/04-dorosti.md).

## شروع سریع

<div dir="ltr">

```bash
make install            # installs uv, Python 3.14 and dependencies
make image              # writes build/kiwi.png (DECIMATION=4 for a quick preview)
make pdf LANG_CODE=fa   # en | de | pt | ru | fa  → build/kiwi-fa-IR.pdf
make view LANG_CODE=en  # compile and open the PDF
make qa                 # ruff + mypy + pytest (coverage ≥ 80 %)
```

</div>

## مستندات

1. [نمای کلی](docs/fa-IR/01-nemaye-koli.md)
2. [معماری کد](docs/fa-IR/02-memari.md)
3. [توسعه و کیفیت](docs/fa-IR/03-tose-e.md)
4. [درستی رونویسی](docs/fa-IR/04-dorosti.md)

</div>
