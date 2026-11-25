[← Voltar: Desenvolvimento e qualidade](03-desenvolvimento.md) · [README](../../README.pt-BR.md) · [English (UK)](../en-GB/04-fidelity.md) · [Deutsch (DE)](../de-DE/04-treue.md) · [Русский (RU)](../ru-RU/04-tochnost.md) · [فارسی (ایران)](../fa-IR/04-dorosti.md)

# Fidelidade da transcrição

Todas as fórmulas foram transcritas da imagem ampliada (1600 × 1600) da obra original; o código Python
implementa exatamente o que está nos PDFs. Uma primeira leitura, feita a partir de uma imagem de 800 × 800,
tinha vários erros (por exemplo `cos(107·Tᵣ + 5r)`, quando o correto é `cos(10·Tᵣ + 5r)`) e foi substituída.

| Elemento | Leitura |
|---|---|
| Mapa de pixels, `F`, `A`, `B`, `u`, `v`, `E`, `Lₛ`, `Tᵣ`, `Uᵣ`, `Kₛ` | Clara |
| Constante `2/58` em `θᵣ` | Pouco legível |
| Deslocamento `y − 8` em `Pᵣ`, `Qᵣ` (pode ser `y − 9`) | Pouco legível |
| Alcance `λᵣ = 29/88 (1 + √(r/100)) − 3/2 \|(r−50)/45\|³` | Agrupamento escolhido para que o contorno do corpo se feche |

Se você tiver o texto original das fórmulas, basta conferir esses três pontos em `feathers.py` e `background.py`.
