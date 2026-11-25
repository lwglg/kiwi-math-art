import re
from pathlib import Path

import pytest

from kiwi.docs_build import FONTS, LANGUAGES


TYPST = Path(__file__).resolve().parents[1] / "typst"
KEY = re.compile(r"^  ([a-z_]+):", re.MULTILINE)


def keys(lang: str) -> set[str]:
    return set(KEY.findall((TYPST / "lang" / f"{lang}.typ").read_text(encoding="utf-8")))


# Optional layout overrides understood by lib/theme.typ.
OPTIONAL = {"font", "size", "leading"}


def test_every_registered_language_has_a_dictionary() -> None:
    files = {p.stem for p in (TYPST / "lang").glob("*.typ")}
    assert files == set(LANGUAGES)


@pytest.mark.parametrize("lang", sorted(LANGUAGES))
def test_dictionary_has_exactly_the_english_keys(lang: str) -> None:
    reference = keys("en")
    assert reference - keys(lang) == set(), f"{lang}: missing keys"
    assert keys(lang) - reference - OPTIONAL == set(), f"{lang}: unknown keys"


@pytest.mark.parametrize("lang", sorted(LANGUAGES))
def test_entry_point_selects_the_dictionary(lang: str) -> None:
    main = (TYPST / "main.typ").read_text(encoding="utf-8")
    assert lang == "en" or f'import "lang/{lang}.typ"' in main


def test_persian_dictionary_selects_a_bundled_font() -> None:
    assert 'font: ("Vazirmatn",)' in (TYPST / "lang" / "fa.typ").read_text(encoding="utf-8")
    assert (FONTS / "Vazirmatn-Regular.ttf").exists()
    assert (FONTS / "Vazirmatn-Bold.ttf").exists()
    assert (FONTS / "OFL.txt").exists()
