import numpy as np

from interpol.lagrange import lagrange_interpolation
from interpol.linear import linear_interpolation


def test_compare_linear_lagrange():
    """Сравнение методов на 2 точках (должны давать одинаковый результат)"""
    x, y = [0, 1], [0, 1]
    points = [0.1, 0.5, 0.9]

    for point in points:
        linear = linear_interpolation(x, y, point)
        lagrange = lagrange_interpolation(x, y, point)
        assert np.isclose(linear, lagrange)


def test_identical_points():
    """Все Y одинаковые (должна быть горизонтальная линия)"""
    x, y = [0, 1, 2], [5, 5, 5]
    test_points = [-1, 0.5, 1.5, 3]

    for point in test_points:
        assert np.isclose(linear_interpolation(x, y, point), 5)
        assert np.isclose(lagrange_interpolation(x, y, point), 5)
