[← Voltar: Visão geral](01-visao-geral.md) · [README](../../README.pt-BR.md) · [English (UK)](../en-GB/02-architecture.md) · [Deutsch (DE)](../de-DE/02-architektur.md) · [Русский (RU)](../ru-RU/02-arhitektura.md) · [فارسی (ایران)](../fa-IR/02-memari.md) · [Próximo: Desenvolvimento e qualidade →](03-desenvolvimento.md)

# Arquitetura do código

| Módulo (`src/kiwi/`) | Responsabilidade | Seção do PDF |
|---|---|---|
| `numerics.py` | chaves suaves `step`/`cutoff`/`dexp` | 2 |
| `canvas.py` | pixel → plano | 1 |
| `transfer.py` | função `F` (real → byte) | 1 |
| `feathers.py` | `δᵣ`, `Tᵣ`, `Uᵣ`, `Jᵣ` | 3 |
| `shading.py` | `Z`, `Lₛ` | 3 |
| `masks.py` | bico `A`, patas `B`, níveis `u`/`v`, olho `E` | 4 |
| `background.py` | fundo desfocado `Kₛ` | 5 |
| `palette.py` | montagem de `Hₛ` | 6 |
| `progress.py` | relatório de progresso | — |
| `render.py`, `imageio.py`, `cli.py` | execução e saída | — |
| `docs_build.py` | compila o Typst | — |
| `tools/spacing.py` (fora do pacote) | espaçamento de instruções para `make format` / `make lint` | — |

Typst (`typst/`): `main.typ` (ponto de entrada), `lib/` (tema, autoria, notação),
`sections/` (uma seção por arquivo, só matemática) e `lang/` (textos por idioma).
Para adicionar um idioma de PDF, crie `lang/<código>.typ` e registre-o em `main.typ` e `docs_build.py`.
Idiomas da direita para a esquerda (persa) não exigem trabalho extra de layout: o Typst deduz a direção de `lang`, e o dicionário só define uma `font` de escrita arábica (e `size`, `leading`). `typst/fonts/` contém a fonte Vazirmatn (SIL OFL); as compilações ignoram as fontes do sistema, então os PDFs são reproduzíveis.

A documentação em Markdown fica em `docs/<idioma>/`; o `README.md` é a porta de entrada padrão (en-GB).
