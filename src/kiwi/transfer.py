"""Transfer function F mapping a channel value to a byte (from the source image).

F(x) = floor(255 e^{-e^{-1000 x}} |x|^{e^{-e^{1000 (x-1)}}})
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from kiwi.numerics import Array, cutoff, step


def channel_to_byte(value: Array) -> NDArray[np.uint8]:
    v = np.nan_to_num(np.asarray(value, dtype=np.float64), nan=0.0)

    scaled = 255.0 * step(v) * np.power(np.abs(v), cutoff(v - 1.0))

    return np.clip(np.floor(scaled), 0, 255).astype(np.uint8)
