import numpy as np

from kiwi import masks


def test_beak_is_on_its_axis_and_not_far_above() -> None:
    x = np.array([-1.7])
    assert masks.beak(x, masks.beak_axis(x))[0] > 0.9
    assert masks.beak(x, masks.beak_axis(x) + 1.0)[0] < 1e-6


def test_beak_is_cut_off_at_both_ends() -> None:
    y = masks.beak_axis(np.array([-2.5, -1.0]))
    assert masks.beak(np.array([-2.5]), y[:1])[0] < 1e-6
    assert masks.beak(np.array([-1.0]), y[1:])[0] < 1e-6


def test_beak_line_marks_the_axis() -> None:
    x = np.array([-1.7])
    assert masks.beak_line(x, masks.beak_axis(x))[0] > 0.5
    assert masks.beak_line(x, masks.beak_axis(x) + 0.1)[0] < 1e-6


def test_legs_exist_below_the_body_only() -> None:
    x = np.linspace(-0.5, 0.8, 200)
    y = np.linspace(-1.0, -0.2, 200)
    gx, gy = np.meshgrid(x, y)
    b = masks.legs(gx, gy)
    assert b.max() > 0.5
    assert masks.legs(np.array([0.0]), np.array([0.9]))[0] < 1e-6


def test_outside_bird_is_zero_inside_head_and_body() -> None:
    assert masks.outside_bird(np.array([-1.0]), np.array([0.25]))[0] < 1e-6
    assert masks.outside_bird(np.array([0.0]), np.array([0.0]))[0] < 1e-6
    assert masks.outside_bird(np.array([1.5]), np.array([0.9]))[0] > 0.99


def test_eye_cutout_is_zero_at_the_eye_centre() -> None:
    assert masks.eye_cutout(np.array([-1.0]), np.array([0.25]))[0] < 1e-6
    assert masks.eye_cutout(np.array([0.0]), np.array([0.0]))[0] > 0.99
