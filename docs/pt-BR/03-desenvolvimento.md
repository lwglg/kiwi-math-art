[← Voltar: Arquitetura do código](02-arquitetura.md) · [README](../../README.pt-BR.md) · [English (UK)](../en-GB/03-development.md) · [Deutsch (DE)](../de-DE/03-entwicklung.md) · [Русский (RU)](../ru-RU/03-razrabotka.md) · [فارسی (ایران)](../fa-IR/03-tose-e.md) · [Próximo: Fidelidade da transcrição →](04-fidelidade.md)

# Desenvolvimento e qualidade

- Gerenciador: [`uv`](https://docs.astral.sh/uv/), Python 3.14 (`.python-version`).
- `make lint` — Ruff (`ruff.toml`); `make format` formata.
- Estilo de código: o Ruff formata e faz lint, e também aplica as regras de linhas em branco em torno de definições (E30x).
  O Ruff nunca insere linhas em branco entre instruções comuns; por isso `tools/spacing.py` aplica o estilo da casa dentro
  de funções: uma linha em branco entre instruções, exceto em sequências de chamadas à mesma função e em um objeto seguido
  das chamadas que o configuram (ex.: `parser = ...` e depois `parser.add_argument(...)`). `make format` o executa antes
  de `ruff format`; `make lint` o executa em modo `--check`.
- `make typecheck` — Mypy estrito (`mypy.ini`).
- `make test` — Pytest (`pytest.ini`), falha abaixo de 80 % de cobertura.
- `make qa` roda tudo; o mesmo é executado no GitHub Actions (`.github/workflows/ci.yml`),
  que também compila os PDFs dos cinco idiomas.
- O Python não tem versões LTS oficiais; usa-se a última versão estável.
- A renderização completa (`make image`) leva alguns minutos; use `DECIMATION=4` para prévias.
- Progresso: `make image` e `make pdf` mostram o progresso de cada etapa no stderr (barras com porcentagem, tempo
  decorrido e ETA no terminal; uma linha a cada 10 % em logs e no CI). `make pdf-all` mostra etapas `[i/10]` com um
  indicador giratório enquanto o Typst compila. Use `QUIET=1` (ou `--quiet` em `kiwi` / `kiwi-docs`) para silenciar.
