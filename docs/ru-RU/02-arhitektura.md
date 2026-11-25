[← Назад: Обзор](01-obzor.md) · [README](../../README.ru-RU.md) · [English (UK)](../en-GB/02-architecture.md) · [Português (Brasil)](../pt-BR/02-arquitetura.md) · [Deutsch (DE)](../de-DE/02-architektur.md) · [فارسی (ایران)](../fa-IR/02-memari.md) · [Далее: Разработка и качество →](03-razrabotka.md)

# Архитектура кода

| Модуль (`src/kiwi/`) | Назначение | Раздел PDF |
|---|---|---|
| `numerics.py` | гладкие переключатели `step`/`cutoff`/`dexp` | 2 |
| `canvas.py` | пиксель → плоскость | 1 |
| `transfer.py` | функция `F` (вещественное число → байт) | 1 |
| `feathers.py` | `δᵣ`, `Tᵣ`, `Uᵣ`, `Jᵣ` | 3 |
| `shading.py` | `Z`, `Lₛ` | 3 |
| `masks.py` | клюв `A`, лапы `B`, уровни `u`/`v`, глаз `E` | 4 |
| `background.py` | размытый фон `Kₛ` | 5 |
| `palette.py` | сборка `Hₛ` | 6 |
| `progress.py` | отчёт о ходе выполнения | — |
| `render.py`, `imageio.py`, `cli.py` | запуск и вывод | — |
| `docs_build.py` | компиляция исходников Typst | — |
| `tools/spacing.py` (вне пакета) | пустые строки между операторами для `make format` / `make lint` | — |

Typst (`typst/`): `main.typ` (точка входа), `lib/` (оформление, авторство, обозначения),
`sections/` (по одному разделу на файл, только математика) и `lang/` (текст на каждом языке).
Чтобы добавить язык PDF, создайте `lang/<код>.typ` и зарегистрируйте его в `main.typ` и `docs_build.py`.
Языки с письмом справа налево (персидский) не требуют дополнительной вёрстки: Typst определяет направление по `lang`, а словарь лишь задаёт шрифт `font` с арабской письменностью (и `size`, `leading`). В `typst/fonts/` лежит встроенный шрифт Vazirmatn (SIL OFL); при сборке системные шрифты игнорируются, поэтому PDF воспроизводимы.

Документация в формате Markdown находится в `docs/<язык>/`; `README.md` — точка входа по умолчанию (en-GB).
