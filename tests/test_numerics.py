import numpy as np

from kiwi.numerics import cutoff, exp_clip, step


def test_step_is_a_smooth_heaviside() -> None:
    assert step(0.5) > 0.999
    assert step(-0.5) < 1e-6


def test_cutoff_is_the_complement() -> None:
    assert cutoff(-0.5) > 0.999
    assert cutoff(0.5) < 1e-6


def test_exp_clip_never_overflows() -> None:
    assert np.isfinite(exp_clip(1e6))
    assert exp_clip(-1e6) >= 0.0
