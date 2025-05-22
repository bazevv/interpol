import numpy as np
import pytest

from interpol.lagrange import lagrange_interpolation


@pytest.fixture()
def quadratic_data():
    return [0.0, 1.0, 2.0], [0.0, 1.0, 4.0]  # y = x^2


def test_lagrange_at_nodes(quadratic_data):
    x, y = quadratic_data
    for xi, yi in zip(x, y):
        assert np.isclose(lagrange_interpolation(x, y, xi), yi)


def test_lagrange_between_nodes(quadratic_data):
    x, y = quadratic_data
    assert np.isclose(lagrange_interpolation(x, y, 0.5), 0.25)


def test_lagrange_extrapolation(quadratic_data):
    x, y = quadratic_data
    assert np.isclose(lagrange_interpolation(x, y, -1.0), 1.0)
    assert np.isclose(lagrange_interpolation(x, y, 3.0), 9.0)


def test_lagrange_single_point():
    with pytest.raises(ValueError):
        lagrange_interpolation([1.0], [1.0], 0.5)


def test_lagrange_empty_input():
    with pytest.raises(ValueError):
        lagrange_interpolation([], [], 0.5)


def test_lagrange_duplicate_x():
    with pytest.raises(ValueError):
        lagrange_interpolation([0.0, 0.0], [1.0, 2.0], 0.5)


def test_lagrange_mismatched_lengths():
    with pytest.raises(ValueError):
        lagrange_interpolation([0.0, 1.0], [0.0], 0.5)


def test_lagrange_array_input(quadratic_data):
    x, y = quadratic_data
    x_new = np.array([0.5, 1.5])
    result = lagrange_interpolation(x, y, x_new)
    expected = np.array([0.25, 2.25])
    assert np.allclose(result, expected)
