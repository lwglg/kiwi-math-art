"""K_s(x, y): the blurred (bokeh) background, a sum of 40 oriented lattices.

K_s = sum_{r=1}^{40} 9/(54 - 30(s-1) + 32(s^2-s)) (3/5 + sin(2r+4s)/5 + sin((2+5s)r)/5)
      * exp(-e^{-15 (S1 * S2 - 1/10)}),
S1 = sin^10(sin 2r + (3 + sin r^2)(sin 7r * x/2 + cos 7r * (y-8)/2)),
S2 = sin^10(sin 3r + (3 + 2 sin r^2)(sin 7r * (y-8)/2 - cos 7r * x/2)).
"""

from __future__ import annotations

import numpy as np

from kiwi.numerics import Array, dexp
from kiwi.progress import NullReporter, Reporter


N_BLOBS = 40


def blob_mask(x: Array, y: Array, r: int) -> Array:
    """The s-independent factor of the r-th term."""
    a = np.sin(7.0 * r) * x / 2.0 + np.cos(7.0 * r) * (y - 8.0) / 2.0

    b = np.sin(7.0 * r) * (y - 8.0) / 2.0 - np.cos(7.0 * r) * x / 2.0

    s1 = np.sin(np.sin(2.0 * r) + (3.0 + np.sin(r**2)) * a) ** 10

    s2 = np.sin(np.sin(3.0 * r) + (3.0 + 2.0 * np.sin(r**2)) * b) ** 10

    return dexp(-15.0 * (s1 * s2 - 1.0 / 10.0))


def weight(s: int, r: int) -> float:
    """The scalar weight of the r-th blob in channel s."""
    base = 9.0 / (54.0 - 30.0 * (s - 1.0) + 32.0 * (s**2 - s))

    return float(
        base * (3.0 / 5.0 + np.sin(2.0 * r + 4.0 * s) / 5.0 + np.sin((2.0 + 5.0 * s) * r) / 5.0)
    )


def field(x: Array, y: Array, reporter: Reporter | None = None) -> list[Array]:
    """Return ``[K_0, K_1, K_2]``."""
    rep = reporter or NullReporter()

    total = [np.zeros_like(x) for _ in range(3)]

    rep.stage("Background (K_s)", N_BLOBS)

    for r in range(1, N_BLOBS + 1):
        mask = blob_mask(x, y, r)
        for s in range(3):
            total[s] += weight(s, r) * mask
        rep.advance()

    rep.end(f"{N_BLOBS} bokeh patches")

    return total
