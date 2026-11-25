# kiwi-math-art

[🇬🇧 English (UK)](README.md) · [🇧🇷 Português (Brasil)](README.pt-BR.md) · [🇩🇪 Deutsch (DE)](README.de-DE.md) · **🇷🇺 Русский (RU)** · [🇮🇷 فارسی (ایران)](README.fa-IR.md)

Математическая документация (Typst, на en-GB, de-DE, pt-BR, ru-RU и fa-IR) и реализация на Python киви, нарисованного
только формулами, по работе [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh).

Оригинальная работа: **[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)** — [LinkedIn](https://www.linkedin.com/in/hamidnaderiyeganeh) · [X](https://x.com/naderi_yeganeh) · [YouTube](https://www.youtube.com/@naderiyeganeh)

Расширенный проект: **Guilherme Lima Gonçalves** — [LinkedIn](https://linkedin.com/in/guligon90) · [GitHub](https://github.com/lwglg) · [Личная страница](https://lwglg.github.io/portfolio-spa)

> Формулы транскрибированы с увеличенного изображения; несколько мелких констант плохо читаются. См. [Точность](docs/ru-RU/04-tochnost.md).

## Быстрый старт

```bash
make install            # устанавливает uv, Python 3.14 и зависимости
make image              # создаёт build/kiwi.png (DECIMATION=4 для быстрого предпросмотра)
make pdf LANG_CODE=ru   # en | de | pt | ru | fa  → build/kiwi-ru-RU.pdf
make view LANG_CODE=en  # компилирует и открывает PDF
make qa                 # ruff + mypy + pytest (покрытие ≥ 80 %)
```

## Документация

1. [Обзор](docs/ru-RU/01-obzor.md)
2. [Архитектура кода](docs/ru-RU/02-arhitektura.md)
3. [Разработка и качество](docs/ru-RU/03-razrabotka.md)
4. [Точность транскрипции](docs/ru-RU/04-tochnost.md)
