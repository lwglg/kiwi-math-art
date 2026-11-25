"""Feather strokes: delta_r, T_r, U_r and the stroke function J_r (all transcribed)."""

from __future__ import annotations

import numpy as np

from kiwi.numerics import Array, dexp


N_FEATHERS = 100


def offset(x: Array, r: int) -> Array:
    """delta_r = x + (60 - r)/40."""
    return x + (60.0 - r) / 40.0


def warped_y(x: Array, y: Array, r: int) -> Array:
    """T_r = y + 4/5 (3 + cos((12 + 5 cos 2r^2) y + 5 cos 14r)) delta_r^3."""
    wave = 3.0 + np.cos((12.0 + 5.0 * np.cos(2.0 * r**2)) * y + 5.0 * np.cos(14.0 * r))

    return np.asarray(y + 0.8 * wave * offset(x, r) ** 3, dtype=np.float64)


def phase(x: Array, y: Array, r: int) -> Array:
    """U_r = (140 - 30 atan(3(r-20)/10) - 30 e^{-y^2}) T_r + cos(10 T_r + 5r) + 10 cos r^2."""
    t = warped_y(x, y, r)

    gain = 140.0 - 30.0 * np.arctan(3.0 * (r - 20.0) / 10.0) - 30.0 * np.exp(-(y**2))

    return np.asarray(
        gain * t + np.cos(10.0 * t + 5.0 * r) + 10.0 * np.cos(float(r) ** 2), dtype=np.float64
    )


def head_hole(x: Array, y: Array) -> Array:
    """W = (x + 1 - 1/(70|y-2/5| + 4))^2 + 2|y-1/4|^{3+x} - 11/100."""
    with np.errstate(all="ignore"):
        return np.asarray(
            (x + 1.0 - 1.0 / (70.0 * np.abs(y - 2.0 / 5.0) + 4.0)) ** 2
            + 2.0 * np.abs(y - 0.25) ** (3.0 + x)
            - 11.0 / 100.0,
            dtype=np.float64,
        )


def extent(r: int) -> float:
    """29/88 (1 + sqrt(r/100)) - 3/2 |(r-50)/45|^3: the vertical reach of stroke r."""
    return float(29.0 / 88.0 * (1.0 + np.sqrt(r / 100.0)) - 1.5 * abs((r - 50.0) / 45.0) ** 3)


def stroke(x: Array, y: Array, r: int) -> Array:
    """J_r = e^{-e^{-1000(r-1/2)} - e^{-5(sin U_r - 2/5 - 2/58 atan(2/5 (r-15)) - 4 delta^2)}
    - e^{-100 delta}} (1 - e^{-e^{-200(|T_r| - extent)} - e^{-40 W}})."""
    t = warped_y(x, y, r)

    d = offset(x, r)

    lead = dexp(-1000.0 * (r - 0.5))

    ridge_arg = (
        np.sin(phase(x, y, r))
        - 2.0 / 5.0
        - 2.0 / 58.0 * np.arctan(2.0 / 5.0 * (r - 15.0))
        - 4.0 * d**2
    )

    ridge = dexp(-5.0 * ridge_arg)

    start = dexp(-100.0 * d)

    inside = dexp(-200.0 * (np.abs(t) - extent(r))) * dexp(-40.0 * head_hole(x, y))

    return np.asarray(lead * ridge * start * (1.0 - inside), dtype=np.float64)
