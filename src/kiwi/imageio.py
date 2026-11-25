"""Saving the rendered array to disk."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from numpy.typing import NDArray
from PIL import Image


def save_png(pixels: NDArray[np.uint8], path: Path) -> Path:
    """Write ``pixels`` as PNG, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)

    Image.fromarray(pixels, mode="RGB").save(path, format="PNG")

    return path
