"""Region functions A (beak), B (legs) and the head/body/eye cut-outs.

Every constant below is transcribed from the source image.
"""

from __future__ import annotations

import numpy as np

from kiwi.numerics import Array, cutoff, dexp, step


def beak_axis(x: Array) -> Array:
    """Centre line of the beak: y = 36/100 - x^2/10."""
    return 36.0 / 100.0 - x**2 / 10.0


def beak_line(x: Array, y: Array) -> Array:
    """exp(-exp(1000(|y - 9/25 + x^2/10| - 1/2000))): the thin line along the beak."""
    return cutoff(np.abs(y - 9.0 / 25.0 + x**2 / 10.0) - 1.0 / 2000.0, k=1000.0)


def beak(x: Array, y: Array) -> Array:
    """A(x, y) = exp(-e^{100(|y-36/100+x^2/10| - |x+21/10|^{3/10}/20 - 7/50 (x+21/10)^4)}
    - e^{20(x+123/100)} - e^{-1000(x+21/10)})."""
    d = x + 21.0 / 10.0

    half_width = np.abs(d) ** (3.0 / 10.0) / 20.0 + 7.0 / 50.0 * d**4

    e1 = np.exp(np.clip(100.0 * (np.abs(y - 36.0 / 100.0 + x**2 / 10.0) - half_width), -700, 700))

    e2 = np.exp(np.clip(20.0 * (x + 123.0 / 100.0), -700, 700))

    e3 = np.exp(np.clip(-1000.0 * d, -700, 700))

    return np.asarray(np.exp(-e1 - e2 - e3), dtype=np.float64)


def leg_profile(x: Array, y: Array) -> Array:
    """q(x, y) = y + 4 |x - 1/5 + 1/2 |y + 4/5|^{13/10}| (the slanted leg axis)."""
    inner = x - 1.0 / 5.0 + 0.5 * np.abs(y + 4.0 / 5.0) ** (13.0 / 10.0)

    return y + 4.0 * np.abs(inner)


def legs(x: Array, y: Array) -> Array:
    """B(x, y) = exp(-e^{20(|q| - 9/10 + sin(200y+5x+5 sin(34y+4x))/200 - (10y+2)/11)}
    - e^{50(y + 1/2 - x^2)})."""
    ripple = np.sin(200.0 * y + 5.0 * x + 5.0 * np.sin(34.0 * y + 4.0 * x)) / 200.0

    e1 = np.exp(
        np.clip(
            20.0 * (np.abs(leg_profile(x, y)) - 9.0 / 10.0 + ripple - (10.0 * y + 2.0) / 11.0),
            -700,
            700,
        )
    )

    e2 = np.exp(np.clip(50.0 * (y + 0.5 - x**2), -700, 700))

    return np.asarray(np.exp(-e1 - e2), dtype=np.float64)


def head_level(x: Array, y: Array) -> Array:
    """u = (x+1)^2 + 2|y-1/4|^{3+x} - 1/10 (negative inside the head)."""
    with np.errstate(all="ignore"):
        return np.asarray(
            (x + 1.0) ** 2 + 2.0 * np.abs(y - 0.25) ** (3.0 + x) - 0.1, dtype=np.float64
        )


def body_level(x: Array, y: Array) -> Array:
    """v = (x+6/25)^2 + 8/5 |y|^{2+x} - 7/10 (negative inside the body)."""
    with np.errstate(all="ignore"):
        return np.asarray(
            (x + 6.0 / 25.0) ** 2 + 8.0 / 5.0 * np.abs(y) ** (2.0 + x) - 0.7, dtype=np.float64
        )


def outside_bird(x: Array, y: Array) -> Array:
    """exp(-e^{-40u} - e^{-17v}): 1 outside head and body, 0 inside either."""
    return dexp(-40.0 * head_level(x, y)) * dexp(-17.0 * body_level(x, y))


def eye_cutout(x: Array, y: Array) -> Array:
    """exp(-e^{-2000((x+1)^2 + 64/1000 |y-1/4| - 1/500)}): 0 inside the eye."""
    return step((x + 1.0) ** 2 + 64.0 / 1000.0 * np.abs(y - 0.25) - 1.0 / 500.0, k=2000.0)
