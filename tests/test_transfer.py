import numpy as np

from kiwi.transfer import channel_to_byte


def test_negative_values_become_zero() -> None:
    assert channel_to_byte(np.array([-0.5]))[0] == 0


def test_values_above_one_saturate() -> None:
    assert channel_to_byte(np.array([3.0]))[0] == 255


def test_midpoint_is_scaled_linearly() -> None:
    assert channel_to_byte(np.array([0.5]))[0] in (126, 127)


def test_nan_is_treated_as_zero() -> None:
    assert channel_to_byte(np.array([np.nan]))[0] == 0
