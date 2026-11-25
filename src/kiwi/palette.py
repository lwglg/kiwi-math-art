"""Assembly of the channel function H_s(x, y), exactly as in the source image.

H_s = ((16-2s^2+s)/20 + 4y - 36/25 + 2x^2/5 - line) A Z
    + Z B/10 (3/2 - (4s^2+5s)/30) (1 + 8 (e^{-e^{-50(x-3/20)}} - 1/2) q)
    + ((2-s)/10 + (x/5 + 53/50) K_s e^{-e^{-40u} - e^{-17v}}) (1 - A - B) Z
    + L_s e^{-e^{-2000((x+1)^2 + 64/1000 |y-1/4| - 1/500)}}
"""

from __future__ import annotations

from kiwi import background, masks
from kiwi.numerics import Array, step
from kiwi.progress import NullReporter, Reporter
from kiwi.shading import covered_and_painted


def beak_term(s: int, x: Array, y: Array, a: Array, z: Array) -> Array:
    gradient = (16.0 - 2.0 * s**2 + s) / 20.0 + 4.0 * y - 36.0 / 25.0 + 2.0 * x**2 / 5.0

    return (gradient - masks.beak_line(x, y)) * a * z


def legs_term(s: int, x: Array, y: Array, b: Array, z: Array) -> Array:
    shade = 3.0 / 2.0 - (4.0 * s**2 + 5.0 * s) / 30.0

    sheen = 1.0 + 8.0 * (step(x - 3.0 / 20.0, k=50.0) - 0.5) * masks.leg_profile(x, y)

    return z * b / 10.0 * shade * sheen


def backdrop_term(s: int, x: Array, y: Array, k: Array, a: Array, b: Array, z: Array) -> Array:
    tone = (2.0 - s) / 10.0 + (x / 5.0 + 53.0 / 50.0) * k * masks.outside_bird(x, y)

    return tone * (1.0 - a - b) * z


def channels(x: Array, y: Array, reporter: Reporter | None = None) -> list[Array]:
    """Return ``[H_0, H_1, H_2]``."""
    rep = reporter or NullReporter()

    z, painted = covered_and_painted(x, y, rep)

    ks = background.field(x, y, rep)

    rep.stage("Masks and channels (H_s)", 3)

    a, b = masks.beak(x, y), masks.legs(x, y)

    eye = masks.eye_cutout(x, y)

    result: list[Array] = []

    for s in range(3):
        result.append(
            beak_term(s, x, y, a, z)
            + legs_term(s, x, y, b, z)
            + backdrop_term(s, x, y, ks[s], a, b, z)
            + painted[s] * eye
        )
        rep.advance()

    rep.end("R, G, B")

    return result


def channel(s: int, x: Array, y: Array) -> Array:
    """Single channel ``H_s``."""
    return channels(x, y)[s]
