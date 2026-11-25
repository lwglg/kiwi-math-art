<div dir="rtl" lang="fa">

[→ بازگشت: معماری کد](02-memari.md) · [README](../../README.fa-IR.md) · [English (UK)](../en-GB/03-development.md) · [Português (Brasil)](../pt-BR/03-desenvolvimento.md) · [Deutsch (DE)](../de-DE/03-entwicklung.md) · [Русский (RU)](../ru-RU/03-razrabotka.md) · [بعدی: درستی رونویسی →](04-dorosti.md)

# توسعه و کیفیت

- مدیر بسته: [`uv`](https://docs.astral.sh/uv/)، پایتون 3.14 (`.python-version`).
- `make lint` — Ruff (`ruff.toml`)؛ `make format` قالب‌بندی می‌کند.
- سبک کد: Ruff قالب‌بندی و بررسی می‌کند و قواعد خط خالی پیرامون تعریف‌ها (E30x) را هم اعمال می‌کند. Ruff هرگز بین دستورهای معمولی خط خالی نمی‌گذارد؛ بنابراین `tools/spacing.py` سبک پروژه را درون بدنه‌ی تابع‌ها اعمال می‌کند: یک خط خالی بین دستورها، مگر در دنباله‌ی فراخوانی‌های یک تابع و شیئی که بلافاصله فراخوانی‌های پیکربندی‌کننده‌اش پس از آن می‌آید (مثلاً `parser = ...` و سپس `parser.add_argument(...)`). `make format` آن را پیش از `ruff format` اجرا می‌کند و `make lint` در حالت `--check`.
- `make typecheck` — Mypy سخت‌گیر (`mypy.ini`).
- `make test` — Pytest (`pytest.ini`)؛ زیر 80 % پوشش شکست می‌خورد.
- `make qa` همه‌چیز را اجرا می‌کند؛ GitHub Actions (`.github/workflows/ci.yml`) همین کار را می‌کند و افزون بر آن PDF را به هر پنج زبان می‌سازد.
- پایتون نسخه‌ی LTS رسمی ندارد، پس آخرین نسخه‌ی پایدار به کار می‌رود.
- رندر کامل (`make image`) چند دقیقه طول می‌کشد؛ برای پیش‌نمایش از `DECIMATION=4` استفاده کنید.
- پیشرفت: `make image` و `make pdf` پیشرفت هر مرحله را روی stderr چاپ می‌کنند (در ترمینال نوار با درصد، زمان سپری‌شده و ETA؛ در لاگ و CI یک خط به‌ازای هر 10 %). `make pdf-all` مراحل `[i/10]` را با یک چرخنده نشان می‌دهد تا Typst کامپایل کند. با `QUIET=1` (یا `--quiet` در `kiwi` / `kiwi-docs`) خروجی ساکت می‌شود.

</div>
