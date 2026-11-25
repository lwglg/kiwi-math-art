[← Zurück: Überblick](01-uebersicht.md) · [README](../../README.de-DE.md) · [English (UK)](../en-GB/02-architecture.md) · [Português (Brasil)](../pt-BR/02-arquitetura.md) · [Русский (RU)](../ru-RU/02-arhitektura.md) · [فارسی (ایران)](../fa-IR/02-memari.md) · [Weiter: Entwicklung und Qualität →](03-entwicklung.md)

# Code-Architektur

| Modul (`src/kiwi/`) | Aufgabe | PDF-Abschnitt |
|---|---|---|
| `numerics.py` | glatte Schalter `step`/`cutoff`/`dexp` | 2 |
| `canvas.py` | Pixel → Ebene | 1 |
| `transfer.py` | Funktion `F` (reell → Byte) | 1 |
| `feathers.py` | `δᵣ`, `Tᵣ`, `Uᵣ`, `Jᵣ` | 3 |
| `shading.py` | `Z`, `Lₛ` | 3 |
| `masks.py` | Schnabel `A`, Beine `B`, Niveaus `u`/`v`, Auge `E` | 4 |
| `background.py` | unscharfer Hintergrund `Kₛ` | 5 |
| `palette.py` | Zusammensetzen von `Hₛ` | 6 |
| `progress.py` | Fortschrittsanzeige | — |
| `render.py`, `imageio.py`, `cli.py` | Ausführung und Ausgabe | — |
| `docs_build.py` | kompiliert die Typst-Quellen | — |
| `tools/spacing.py` (außerhalb des Pakets) | Anweisungsabstände für `make format` / `make lint` | — |

Typst (`typst/`): `main.typ` (Einstiegspunkt), `lib/` (Layout, Autorenangaben, Notation),
`sections/` (ein Abschnitt pro Datei, nur Mathematik) und `lang/` (Text je Sprache).
Für eine weitere PDF-Sprache `lang/<Code>.typ` anlegen und in `main.typ` sowie `docs_build.py` eintragen.
Rechts-nach-links-Sprachen (Persisch) brauchen keine zusätzliche Layoutarbeit: Typst leitet die Richtung aus `lang` ab, und das Wörterbuch setzt nur eine arabischschriftfähige `font` (sowie `size`, `leading`). `typst/fonts/` enthält die mitgelieferte Schrift Vazirmatn (SIL OFL); Builds ignorieren Systemschriften, die PDFs sind also reproduzierbar.

Die Markdown-Dokumentation liegt in `docs/<Sprache>/`; `README.md` ist der Standard-Einstieg (en-GB).
