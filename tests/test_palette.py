import numpy as np

from kiwi import background
from kiwi.palette import channel, channels
from kiwi.shading import covered_and_painted


def test_background_blobs_are_bounded_and_finite() -> None:
    x, y = np.meshgrid(np.linspace(-2, 2, 8), np.linspace(-1, 1, 8))
    for k in background.field(x, y):
        assert np.isfinite(k).all()
        assert k.min() >= -1e-9


def test_blob_weight_matches_the_formula_for_one_term() -> None:
    expected = 9 / 84 * (3 / 5 + np.sin(2) / 5 + np.sin(2) / 5)
    assert np.isclose(background.weight(0, 1), expected)


def test_coverage_is_a_fraction() -> None:
    x, y = np.meshgrid(np.linspace(-1, 1, 6), np.linspace(-0.5, 0.5, 6))
    z, painted = covered_and_painted(x, y)
    assert z.min() >= -1e-9
    assert z.max() <= 1.0 + 1e-9
    assert len(painted) == 3


def test_channels_are_finite_and_consistent() -> None:
    x, y = np.meshgrid(np.linspace(-2, 2, 6), np.linspace(-1, 1, 6))
    hs = channels(x, y)
    for s in range(3):
        assert np.isfinite(hs[s]).all()
        assert np.allclose(channel(s, x, y), hs[s])


def test_beak_is_creamy_and_eye_is_dark() -> None:
    beak = [h[0, 0] for h in channels(np.array([[-1.9]]), np.array([[0.36 - 1.9**2 / 10 + 0.02]]))]
    assert beak[0] > 0.6
    assert beak[0] > beak[2]
    eye = [h[0, 0] for h in channels(np.array([[-1.0]]), np.array([[0.25]]))]
    assert max(eye) < 0.3
