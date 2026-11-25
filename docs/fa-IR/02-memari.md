<div dir="rtl" lang="fa">

[→ بازگشت: نمای کلی](01-nemaye-koli.md) · [README](../../README.fa-IR.md) · [English (UK)](../en-GB/02-architecture.md) · [Português (Brasil)](../pt-BR/02-arquitetura.md) · [Deutsch (DE)](../de-DE/02-architektur.md) · [Русский (RU)](../ru-RU/02-arhitektura.md) · [بعدی: توسعه و کیفیت →](03-tose-e.md)

# معماری کد

| ماژول (`src/kiwi/`) | وظیفه | بخش PDF |
|---|---|---|
| `numerics.py` | کلیدهای هموار `step`/`cutoff`/`dexp` | 2 |
| `canvas.py` | پیکسل ← صفحه | 1 |
| `transfer.py` | تابع `F` (عدد حقیقی ← بایت) | 1 |
| `feathers.py` | `δᵣ`، `Tᵣ`، `Uᵣ`، `Jᵣ` | 3 |
| `shading.py` | `Z`، `Lₛ` | 3 |
| `masks.py` | نوک `A`، پاها `B`، ترازهای `u`/`v`، چشم `E` | 4 |
| `background.py` | پس‌زمینه‌ی محو `Kₛ` | 5 |
| `palette.py` | سرهم‌کردن `Hₛ` | 6 |
| `progress.py` | گزارش پیشرفت | — |
| `render.py`، `imageio.py`، `cli.py` | اجرا و خروجی | — |
| `docs_build.py` | کامپایل منابع Typst | — |
| `tools/spacing.py` (بیرون از بسته) | فاصله‌ی دستورها برای `make format` / `make lint` | — |

Typst (`typst/`): ‎`main.typ` (نقطه‌ی ورود)، ‎`lib/` (قالب، اطلاعات نویسندگان، نمادگذاری)،
‎`sections/` (هر بخش در یک فایل، فقط ریاضی) و ‎`lang/` (متن هر زبان).
برای افزودن زبان PDF، فایل ‎`lang/<code>.typ` را بسازید و در ‎`main.typ` و ‎`docs_build.py` ثبت کنید.
زبان‌های راست‌به‌چپ (فارسی) کار چیدمان اضافه نمی‌خواهند: Typst جهت را از ‎`lang` می‌فهمد و دیکشنری فقط یک ‎`font` با خط عربی (و ‎`size` و ‎`leading`) تعیین می‌کند. پوشه‌ی ‎`typst/fonts/` فونت همراه Vazirmatn (SIL OFL) را دارد؛ در ساخت، فونت‌های سیستم نادیده گرفته می‌شوند و بنابراین PDFها بازتولیدپذیرند.

مستندات Markdown در ‎`docs/<language>/` قرار دارد؛ ‎`README.md` نقطه‌ی ورود پیش‌فرض (en-GB) است.

</div>
