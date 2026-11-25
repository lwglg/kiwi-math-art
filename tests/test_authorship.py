import re
from pathlib import Path

import pytest

from kiwi.docs_build import LANGUAGES


ROOT = Path(__file__).resolve().parents[1]
WIKIPEDIA = "https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh"
LINKED = f"[Hamid Naderi Yeganeh, PhD]({WIKIPEDIA})"
MARKDOWN = sorted([*ROOT.glob("README*.md"), *(ROOT / "docs").rglob("*.md")])


@pytest.mark.parametrize("path", MARKDOWN, ids=lambda p: str(p.relative_to(ROOT)))
def test_markdown_always_links_the_original_author(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    plain = text.replace(LINKED, "")
    assert "Hamid Naderi Yeganeh" not in plain, "unlinked mention of the original author"


def test_every_readme_credits_the_original_author() -> None:
    for path in ROOT.glob("README*.md"):
        assert LINKED in path.read_text(encoding="utf-8"), path.name


@pytest.mark.parametrize("lang", sorted(LANGUAGES))
def test_pdf_footnote_cites_ucl_and_wikipedia(lang: str) -> None:
    text = (ROOT / "typst" / "lang" / f"{lang}.typ").read_text(encoding="utf-8")
    footnote = re.search(r"original_footnote: (\[.*\]),\n", text)
    assert footnote is not None
    assert "University College London (UCL)" in footnote.group(1)
    assert WIKIPEDIA in footnote.group(1)
    assert "Hamid Naderi Yeganeh, PhD" in text


def test_pdf_title_block_attaches_the_footnote_to_the_name() -> None:
    authors = (ROOT / "typst" / "lib" / "authors.typ").read_text(encoding="utf-8")
    assert "PhD#footnote(t.original_footnote)" in authors
