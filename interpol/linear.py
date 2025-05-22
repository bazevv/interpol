from typing import Union

import numpy as np


def linear_interpolation(x: list[float], y: list[float], x_new: Union[float, list[float]]) -> Union[float, np.ndarray]:
    if len(x) != len(y):
        raise ValueError("Количество x и y точек должно совпадать")
    if len(x) < 2:
        raise ValueError("Для интерполяции нужно минимум 2 точки")

    return np.interp(x_new, x, y)
