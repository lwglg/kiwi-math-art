[← Zurück: Entwicklung und Qualität](03-entwicklung.md) · [README](../../README.de-DE.md) · [English (UK)](../en-GB/04-fidelity.md) · [Português (Brasil)](../pt-BR/04-fidelidade.md) · [Русский (RU)](../ru-RU/04-tochnost.md) · [فارسی (ایران)](../fa-IR/04-dorosti.md)

# Treue der Transkription

Alle Formeln wurden vom vergrößerten Bild (1600 × 1600) des Originalwerks transkribiert; der Python-Code
setzt genau das um, was die PDFs drucken. Eine erste Lesung eines 800 × 800 Pixel großen Bildes enthielt
mehrere Fehler (etwa `cos(107·Tᵣ + 5r)`, wo der richtige Term `cos(10·Tᵣ + 5r)` ist) und wurde ersetzt.

| Element | Lesung |
|---|---|
| Pixelabbildung, `F`, `A`, `B`, `u`, `v`, `E`, `Lₛ`, `Tᵣ`, `Uᵣ`, `Kₛ` | Eindeutig |
| Konstante `2/58` in `θᵣ` | Schlecht lesbar |
| Verschiebung `y − 8` in `Pᵣ`, `Qᵣ` (könnte `y − 9` sein) | Schlecht lesbar |
| Reichweite `λᵣ = 29/88 (1 + √(r/100)) − 3/2 \|(r−50)/45\|³` | Klammerung so gewählt, dass der Körperumriss geschlossen ist |

Liegt der Originaltext der Formeln vor, genügt es, diese drei Punkte in `feathers.py` und `background.py` zu prüfen.
