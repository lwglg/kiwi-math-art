# kiwi-math-art

[🇬🇧 English (UK)](README.md) · [🇧🇷 Português (Brasil)](README.pt-BR.md) · **🇩🇪 Deutsch (DE)** · [🇷🇺 Русский (RU)](README.ru-RU.md) · [🇮🇷 فارسی (ایران)](README.fa-IR.md)

Mathematische Dokumentation (Typst, in en-GB, de-DE, pt-BR, ru-RU und fa-IR) und eine Python-Implementierung eines allein
durch Formeln gezeichneten Kiwis, nach dem Werk von [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh).

Originalwerk: **[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)** — [LinkedIn](https://www.linkedin.com/in/hamidnaderiyeganeh) · [X](https://x.com/naderi_yeganeh) · [YouTube](https://www.youtube.com/@naderiyeganeh)

Erweitertes Projekt von **Guilherme Lima Gonçalves** — [LinkedIn](https://linkedin.com/in/guligon90) · [GitHub](https://github.com/lwglg) · [Persönliche Seite](https://lwglg.github.io/portfolio-spa)

> Die Formeln wurden vom vergrößerten Bild transkribiert; wenige kleine Konstanten sind schlecht lesbar. Siehe [Treue](docs/de-DE/04-treue.md).

## Schnellstart

```bash
make install            # installiert uv, Python 3.14 und Abhängigkeiten
make image              # schreibt build/kiwi.png (DECIMATION=4 für eine schnelle Vorschau)
make pdf LANG_CODE=de   # en | de | pt | ru | fa  → build/kiwi-de-DE.pdf
make view LANG_CODE=pt  # kompiliert und öffnet das PDF
make qa                 # ruff + mypy + pytest (Abdeckung ≥ 80 %)
```

## Dokumentation

1. [Überblick](docs/de-DE/01-uebersicht.md)
2. [Code-Architektur](docs/de-DE/02-architektur.md)
3. [Entwicklung und Qualität](docs/de-DE/03-entwicklung.md)
4. [Treue der Transkription](docs/de-DE/04-treue.md)
