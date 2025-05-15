import numpy as np

from interpol.lagrange import lagrange_interpolation
from interpol.linear import linear_interpolation
from interpol.utils import plot_interpolation


def main():
    # Исходные данные
    x = np.array([0, 1, 2, 3, 4, 5], dtype=float)
    y = np.array([0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589], dtype=float)

    # Точки для интерполяции
    x_new = np.linspace(min(x), max(x), 100)

    # Линейная интерполяция
    y_linear = linear_interpolation(x, y, x_new)
    plot_interpolation(x, y, x_new, y_linear, "Linear")

    # Интерполяция Лагранжа
    y_lagrange = lagrange_interpolation(x, y, x_new)
    plot_interpolation(x, y, x_new, y_lagrange, "Lagrange")


if __name__ == "__main__":
    main()
