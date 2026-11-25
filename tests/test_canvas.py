import pytest

from kiwi.canvas import Canvas


def test_plane_origin_mapping() -> None:
    x, y = Canvas().plane()
    assert x.shape == (1060, 2000)
    assert x[0, 0] == pytest.approx((1 - 1300) / 540)
    assert y[0, 0] == pytest.approx((531 - 1) / 540)


def test_decimation_reduces_size() -> None:
    cv = Canvas(decimation=10)
    assert (cv.out_width, cv.out_height) == (200, 106)


def test_invalid_decimation_rejected() -> None:
    with pytest.raises(ValueError, match="positive"):
        Canvas(decimation=0)
