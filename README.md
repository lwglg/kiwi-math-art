# kiwi-math-art

[![CI - QA pipeline](https://github.com/lwglg/kiwi-math-art/actions/workflows/ci.yml/badge.svg)](https://github.com/lwglg/kiwi-math-art/actions/workflows/ci.yml)

**🇬🇧 English (UK)** · [🇧🇷 Português (Brasil)](README.pt-BR.md) · [🇩🇪 Deutsch (DE)](README.de-DE.md) · [🇷🇺 Русский (RU)](README.ru-RU.md) · [🇮🇷 فارسی (ایران)](README.fa-IR.md)

Mathematical documentation (Typst, in en-GB, de-DE, pt-BR, ru-RU and fa-IR) and a Python implementation of a kiwi drawn
purely by formulas, based on the artwork of [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh).

Original artwork: **[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)** — [LinkedIn](https://www.linkedin.com/in/hamidnaderiyeganeh) · [X](https://x.com/naderi_yeganeh) · [YouTube](https://www.youtube.com/@naderiyeganeh)

Augmented project by **Guilherme Lima Gonçalves** — [LinkedIn](https://linkedin.com/in/guligon90) · [GitHub](https://github.com/lwglg) · [Personal page](https://lwglg.github.io/portfolio-spa)

> The formulas were transcribed from the enlarged image; a few small constants have low legibility. See [Fidelity](docs/en-GB/04-fidelity.md).

## Quick start

```bash
make install            # installs uv, Python 3.14 and dependencies
make image              # writes build/kiwi.png (DECIMATION=4 for a quick preview)
make pdf LANG_CODE=en   # en | de | pt | ru | fa  → build/kiwi-en-GB.pdf
make view LANG_CODE=de  # compile and open the PDF
make qa                 # ruff + mypy + pytest (coverage ≥ 80 %)
```

## Documentation

1. [Overview](docs/en-GB/01-overview.md)
2. [Code architecture](docs/en-GB/02-architecture.md)
3. [Development and quality](docs/en-GB/03-development.md)
4. [Fidelity of the transcription](docs/en-GB/04-fidelity.md)
