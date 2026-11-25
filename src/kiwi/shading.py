"""Z (uncovered share) and L_s (painted share) of the feather strokes."""

from __future__ import annotations

import numpy as np

from kiwi.feathers import N_FEATHERS, offset, phase, stroke, warped_y
from kiwi.numerics import Array, dexp
from kiwi.progress import NullReporter, Reporter


def paint(s: int, x: Array, y: Array, r: int, t: Array, u: Array) -> Array:
    """The colour factor of stroke r in channel s (the four brackets of L_s)."""
    arc = np.arctan((r - 10.0) / 10.0)

    crest = 1.0 + dexp(-30.0 * (y - 64.0 / 100.0 + 1.0 / (5.0 + 100.0 * (x + 29.0 / 50.0) ** 2)))

    lift = 2.0 / 5.0 + 0.5 * dexp(-1000.0 * np.sin(u / 2.0)) + 3.0 / 5.0 * t

    hue = 2.0 ** (2.0 - s) / 10.0 + (1.0 / 5.0 - (s**2 - s) / 60.0) * (0.5 - arc / np.pi)

    ramp = (
        1.0 / 10.0
        + 3.0 / 10.0 * (0.5 - np.arctan(3.0 * (r - 25.0) / 10.0) / np.pi)
        + (7.0 / 2.0 + 7.0 / np.pi * arc) * offset(x, r)
    )

    return np.asarray(crest * lift * hue * ramp, dtype=np.float64)


def covered_and_painted(
    x: Array, y: Array, reporter: Reporter | None = None
) -> tuple[Array, list[Array]]:
    """Return ``(Z, [L_0, L_1, L_2])`` with Z = prod(1 - J_r) and
    L_s = sum_r J_r prod_{u<r}(1 - J_u) paint_{s,r}."""
    rep = reporter or NullReporter()

    uncovered = np.ones_like(x)

    painted = [np.zeros_like(x) for _ in range(3)]

    rep.stage("Feathers (J_r, Z, L_s)", N_FEATHERS)

    for r in range(1, N_FEATHERS + 1):
        weight = stroke(x, y, r) * uncovered
        t = warped_y(x, y, r)
        u = phase(x, y, r)
        for s in range(3):
            painted[s] += weight * paint(s, x, y, r, t, u)
        uncovered = uncovered - weight
        rep.advance()

    rep.end(f"{N_FEATHERS} strokes")

    return uncovered, painted
