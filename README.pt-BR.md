# kiwi-math-art

[🇬🇧 English (UK)](README.md) · **🇧🇷 Português (Brasil)** · [🇩🇪 Deutsch (DE)](README.de-DE.md) · [🇷🇺 Русский (RU)](README.ru-RU.md) · [🇮🇷 فارسی (ایران)](README.fa-IR.md)

Documentação matemática (Typst, em en-GB, de-DE, pt-BR, ru-RU e fa-IR) e implementação em Python de um kiwi desenhado
apenas por fórmulas, a partir da obra de [Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh).

Obra original: **[Hamid Naderi Yeganeh, PhD](https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh)** — [LinkedIn](https://www.linkedin.com/in/hamidnaderiyeganeh) · [X](https://x.com/naderi_yeganeh) · [YouTube](https://www.youtube.com/@naderiyeganeh)

Projeto ampliado por **Guilherme Lima Gonçalves** — [LinkedIn](https://linkedin.com/in/guligon90) · [GitHub](https://github.com/lwglg) · [Página pessoal](https://lwglg.github.io/portfolio-spa)

> As fórmulas foram transcritas da imagem ampliada; poucas constantes pequenas têm legibilidade baixa. Veja [Fidelidade](docs/pt-BR/04-fidelidade.md).

## Início rápido

```bash
make install            # instala uv, Python 3.14 e dependências
make image              # gera build/kiwi.png (DECIMATION=4 para prévia rápida)
make pdf LANG_CODE=pt   # en | de | pt | ru | fa  → build/kiwi-pt-BR.pdf
make view LANG_CODE=en  # compila e abre o PDF
make qa                 # ruff + mypy + pytest (cobertura ≥ 80 %)
```

## Documentação

1. [Visão geral](docs/pt-BR/01-visao-geral.md)
2. [Arquitetura do código](docs/pt-BR/02-arquitetura.md)
3. [Desenvolvimento e qualidade](docs/pt-BR/03-desenvolvimento.md)
4. [Fidelidade da transcrição](docs/pt-BR/04-fidelidade.md)
