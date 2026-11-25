from pathlib import Path

import numpy as np

from kiwi.canvas import Canvas
from kiwi.cli import main
from kiwi.imageio import save_png
from kiwi.render import render_rgb


def test_render_shape_and_dtype() -> None:
    img = render_rgb(Canvas(decimation=40))
    assert img.shape == (27, 50, 3)
    assert img.dtype == np.uint8


def test_save_png_creates_parents(tmp_path: Path) -> None:
    out = save_png(render_rgb(Canvas(decimation=80)), tmp_path / "a" / "b.png")
    assert out.exists()


def test_cli_writes_file(tmp_path: Path) -> None:
    target = tmp_path / "k.png"
    assert main(["-o", str(target), "-d", "80"]) == 0
    assert target.stat().st_size > 0
