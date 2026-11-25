"""Rendering driver: evaluate the three channels on the pixel grid."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from kiwi.canvas import Canvas
from kiwi.palette import channels
from kiwi.progress import NullReporter, Reporter
from kiwi.transfer import channel_to_byte


N_STAGES = 5
"""Stages reported by :func:`render_rgb` (the CLI adds one for saving)."""


def render_rgb(canvas: Canvas | None = None, reporter: Reporter | None = None) -> NDArray[np.uint8]:
    """Return an ``(height, width, 3)`` uint8 array."""
    rep = reporter or NullReporter()

    cv = canvas or Canvas()

    rep.stage("Pixel grid", 1)

    x, y = cv.plane()

    rep.advance()

    rep.end(f"{cv.out_width}x{cv.out_height} = {cv.out_width * cv.out_height:,} pixels")

    hs = channels(x, y, rep)

    rep.stage("Colour transfer (F)", 3)

    planes = []

    for h in hs:
        planes.append(channel_to_byte(h))
        rep.advance()

    rep.end("uint8")

    return np.stack(planes, axis=-1)
