import numpy as np

from kiwi.feathers import extent, head_hole, offset, phase, stroke, warped_y


def test_offset_vanishes_at_the_stroke_origin() -> None:
    assert offset(np.array([-1.0]), 20)[0] == 0.0


def test_warp_is_identity_at_zero_offset() -> None:
    assert warped_y(np.array([-1.0]), np.array([0.3]), 20)[0] == np.float64(0.3)


def test_extent_peaks_mid_body_and_vanishes_at_the_ends() -> None:
    assert extent(55) > 0.5
    assert extent(1) < 0.0
    assert extent(100) < 0.0


def test_stroke_is_bounded() -> None:
    x, y = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-0.5, 0.7, 20))
    j = stroke(x, y, 50)
    assert j.min() >= 0.0
    assert j.max() <= 1.0 + 1e-9


def test_stroke_is_absent_far_from_its_origin() -> None:
    assert stroke(np.array([-1.9]), np.array([0.0]), 60)[0] == 0.0


def test_phase_is_finite() -> None:
    x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
    assert np.isfinite(phase(x, y, 7)).all()


def test_head_hole_is_negative_inside_the_head() -> None:
    assert head_hole(np.array([-1.0]), np.array([0.25]))[0] < 0.0
