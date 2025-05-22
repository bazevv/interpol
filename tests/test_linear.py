import numpy as np
import pytest

from interpol.linear import linear_interpolation


@pytest.mark.parametrize(
    "x,y,x_new,expected",
    [
        ([0.0, 1.0], [0.0, 1.0], 0.5, 0.5),
        ([0.0, 2.0], [0.0, 4.0], 1.0, 2.0),
        ([1.0, 2.0], [1.0, 2.0], 1.0, 1.0),
        ([0.0, 1.0], [1.0, 0.0], 0.5, 0.5),
    ],
)
def test_linear_interpolation(x, y, x_new, expected):
    assert np.isclose(linear_interpolation(x, y, x_new), expected)


def test_linear_extrapolation():
    x, y = [0.0, 1.0], [0.0, 1.0]
    assert np.isclose(linear_interpolation(x, y, 0.5), 0.5)


def test_linear_single_point():
    with pytest.raises(ValueError):
        linear_interpolation([1.0], [1.0], 0.5)


def test_linear_empty_input():
    with pytest.raises(ValueError):
        linear_interpolation([], [], 0.5)
        

def test_linear_mismatched_lengths():
    with pytest.raises(ValueError):
        linear_interpolation([0.0, 1.0], [0.0], 0.5)

def test_linear_array_input():
    x, y = [0.0, 1.0], [0.0, 1.0]
    x_new = np.array([0.2, 0.5, 0.8])
    result = linear_interpolation(x, y, x_new)
    expected = np.array([0.2, 0.5, 0.8])
    assert np.allclose(result, expected)
