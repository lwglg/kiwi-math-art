"""Pixel grid and the pixel-to-plane coordinate map."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from kiwi.numerics import Array


@dataclass(frozen=True)
class Canvas:
    """Raster geometry of the original 2000 x 1060 picture.

    ``decimation`` renders only every ``decimation``-th pixel, which gives
    fast previews with the very same formulas.
    """

    width: int = 2000
    height: int = 1060
    x_origin: float = 1300.0
    y_origin: float = 531.0
    unit: float = 540.0
    decimation: int = 1

    def __post_init__(self) -> None:
        if self.decimation < 1:
            msg = "decimation must be a positive integer"
            raise ValueError(msg)

    @property
    def out_width(self) -> int:
        return -(-self.width // self.decimation)

    @property
    def out_height(self) -> int:
        return -(-self.height // self.decimation)

    def plane(self) -> tuple[Array, Array]:
        """Return ``(x, y)`` arrays of shape ``(out_height, out_width)``.

        ``x = (m - 1300) / 540`` and ``y = (531 - n) / 540`` where ``m`` is
        the (1-based) column and ``n`` the (1-based) row.
        """
        m = 1.0 + self.decimation * np.arange(self.out_width, dtype=np.float64)

        n = 1.0 + self.decimation * np.arange(self.out_height, dtype=np.float64)

        x = (m - self.x_origin) / self.unit

        y = (self.y_origin - n) / self.unit

        grid_x, grid_y = np.meshgrid(x, y)

        return grid_x, grid_y
