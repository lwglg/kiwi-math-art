[← Zurück: Code-Architektur](02-architektur.md) · [README](../../README.de-DE.md) · [English (UK)](../en-GB/03-development.md) · [Português (Brasil)](../pt-BR/03-desenvolvimento.md) · [Русский (RU)](../ru-RU/03-razrabotka.md) · [فارسی (ایران)](../fa-IR/03-tose-e.md) · [Weiter: Treue der Transkription →](04-treue.md)

# Entwicklung und Qualität

- Paketverwaltung: [`uv`](https://docs.astral.sh/uv/), Python 3.14 (`.python-version`).
- `make lint` — Ruff (`ruff.toml`); `make format` formatiert.
- Code-Stil: Ruff formatiert und prüft und erzwingt auch die Leerzeilenregeln um Definitionen (E30x). Ruff fügt zwischen
  gewöhnlichen Anweisungen nie Leerzeilen ein; deshalb wendet `tools/spacing.py` den Hausstil in Funktionskörpern an: eine
  Leerzeile zwischen Anweisungen, außer bei Folgen von Aufrufen derselben Funktion und bei einem Objekt, das direkt von den
  Aufrufen gefolgt wird, die es konfigurieren (z. B. `parser = ...`, dann `parser.add_argument(...)`). `make format` führt es
  vor `ruff format` aus; `make lint` im `--check`-Modus.
- `make typecheck` — strenges Mypy (`mypy.ini`).
- `make test` — Pytest (`pytest.ini`), scheitert unter 80 % Abdeckung.
- `make qa` führt alles aus; GitHub Actions (`.github/workflows/ci.yml`) tut dasselbe und
  kompiliert zusätzlich die PDFs in allen fünf Sprachen.
- Python hat keine offiziellen LTS-Versionen, daher wird die neueste stabile Version verwendet.
- Das vollständige Rendern (`make image`) dauert einige Minuten; für Vorschauen `DECIMATION=4` verwenden.
- Fortschritt: `make image` und `make pdf` geben den Fortschritt jeder Stufe auf stderr aus (Balken mit Prozent,
  verstrichener Zeit und ETA im Terminal; eine Zeile je 10 % in Logs und CI). `make pdf-all` zeigt `[i/10]`-Schritte mit
  einem Spinner, während Typst kompiliert. Mit `QUIET=1` (oder `--quiet` bei `kiwi` / `kiwi-docs`) wird alles stumm.
