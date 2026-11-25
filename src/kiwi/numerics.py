"""Numerically safe primitives used by every other module.

Yeganeh's formulas build smooth switches out of the double exponential
``exp(-exp(a))``. We name it :func:`dexp`:

* ``dexp(-k t)`` is ~1 for ``t > 0`` and ~0 for ``t < 0`` (a smooth step);
* ``dexp(+k t)`` is ~1 for ``t < 0`` and ~0 for ``t > 0``.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


Array = NDArray[np.float64]

EXP_LIMIT = 700.0


def exp_clip(t: Array | float) -> Array:
    """``exp`` with the argument clipped to avoid overflow."""
    value = np.exp(np.clip(np.asarray(t, dtype=np.float64), -EXP_LIMIT, EXP_LIMIT))

    return np.asarray(value, dtype=np.float64)


def dexp(a: Array | float) -> Array:
    """The double exponential ``exp(-exp(a))``; NaNs (from 0**negative) become 0."""
    a = np.nan_to_num(np.asarray(a, dtype=np.float64), nan=0.0, posinf=EXP_LIMIT, neginf=-EXP_LIMIT)

    return np.asarray(np.exp(-exp_clip(a)), dtype=np.float64)


def step(t: Array | float, k: float = 1000.0) -> Array:
    """Smooth Heaviside switch ``exp(-exp(-k t))``: close to 1 where ``t > 0``."""
    return dexp(-k * np.asarray(t, dtype=np.float64))


def cutoff(t: Array | float, k: float = 1000.0) -> Array:
    """Smooth complementary switch ``exp(-exp(k t))``: close to 1 where ``t < 0``."""
    return dexp(k * np.asarray(t, dtype=np.float64))
