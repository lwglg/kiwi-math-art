"""Compile the Typst documentation to PDF.

``kiwi-docs --lang en`` builds one language, ``kiwi-docs --lang all`` builds all
of them. Progress is printed to ``stderr`` unless ``--quiet`` is given.
"""

from __future__ import annotations

import argparse
import time
from collections.abc import Sequence
from pathlib import Path

import typst
from PIL import Image

from kiwi.progress import ConsoleReporter, NullReporter, Reporter, format_duration


LANGUAGES: dict[str, str] = {
    "en": "en-GB",
    "de": "de-DE",
    "pt": "pt-BR",
    "ru": "ru-RU",
    "fa": "fa-IR",
}
ROOT = Path(__file__).resolve().parents[2]
ENTRY = ROOT / "typst" / "main.typ"
IMAGE = ROOT / "build" / "kiwi.png"
FONTS = ROOT / "typst" / "fonts"
STAGES_PER_LANGUAGE = 2


def output_path(lang: str, out_dir: Path) -> Path:
    """Where the PDF for ``lang`` is written, e.g. ``build/kiwi-en-GB.pdf``."""
    if lang not in LANGUAGES:
        msg = f"unsupported language {lang!r}; choose one of {sorted(LANGUAGES)}"
        raise ValueError(msg)

    return out_dir / f"kiwi-{LANGUAGES[lang]}.pdf"


def human_size(n_bytes: int) -> str:
    """``1536`` -> ``1.5 KiB``."""
    size = float(n_bytes)

    for unit in ("B", "KiB", "MiB"):
        if size < 1024 or unit == "MiB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} MiB"  # pragma: no cover


def check_inputs(root: Path | None = None) -> str:
    """Verify the sources exist and describe them; raise with a hint otherwise."""
    base = root or ROOT

    entry, image = base / "typst" / "main.typ", base / "build" / "kiwi.png"

    if not entry.exists():
        msg = f"Typst entry point not found: {entry}"
        raise FileNotFoundError(msg)

    if not image.exists():
        msg = f"image not found: {image} (run `make image` first)"
        raise FileNotFoundError(msg)

    modules = len(list((base / "typst").rglob("*.typ")))

    with Image.open(image) as im:
        width, height = im.size

    return f"{modules} Typst modules, image {width}x{height} ({human_size(image.stat().st_size)})"


def compile_pdf(lang: str, out_dir: Path | None = None, reporter: Reporter | None = None) -> Path:
    """Compile ``typst/main.typ`` for ``lang`` and return the PDF path."""
    rep = reporter or NullReporter()

    target = output_path(lang, out_dir or ROOT / "build")

    name = LANGUAGES[lang]

    rep.stage(f"{name}: checking sources", 1)

    summary = check_inputs()

    rep.advance()

    rep.end(summary)

    rep.stage(f"{name}: compiling PDF")

    target.parent.mkdir(parents=True, exist_ok=True)

    typst.compile(
        ENTRY,
        output=target,
        root=ROOT,
        font_paths=[FONTS],
        ignore_system_fonts=True,
        sys_inputs={"lang": lang},
    )

    rep.end(f"{target.name} ({human_size(target.stat().st_size)})")

    return target


def compile_all(out_dir: Path | None = None, reporter: Reporter | None = None) -> list[Path]:
    """Compile every language, reporting ``[i/N]`` stages."""
    rep = reporter or NullReporter()
    rep.plan(STAGES_PER_LANGUAGE * len(LANGUAGES))

    return [compile_pdf(lang, out_dir, rep) for lang in LANGUAGES]


def main(argv: Sequence[str] | None = None, reporter: Reporter | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kiwi-docs")
    parser.add_argument("-l", "--lang", choices=[*sorted(LANGUAGES), "all"], required=True)
    parser.add_argument("-o", "--out-dir", type=Path, default=None)
    parser.add_argument("-q", "--quiet", action="store_true", help="no progress output")

    args = parser.parse_args(argv)

    rep: Reporter = reporter or (NullReporter() if args.quiet else ConsoleReporter())

    started = time.perf_counter()

    langs = list(LANGUAGES) if args.lang == "all" else [args.lang]

    rep.message(f"kiwi-docs: building {', '.join(LANGUAGES[x] for x in langs)}")

    if args.lang == "all":
        paths = compile_all(args.out_dir, rep)
    else:
        rep.plan(STAGES_PER_LANGUAGE)
        paths = [compile_pdf(args.lang, args.out_dir, rep)]

    elapsed = format_duration(time.perf_counter() - started)

    for path in paths:
        print(f"wrote {path}")

    rep.message(f"done: {len(paths)} PDF(s) in {elapsed}")

    return 0
