import numpy as np
from typing import List, Union

def lagrange_interpolation(
    x: List[float], 
    y: List[float], 
    x_new: Union[float, List[float]]
) -> Union[float, np.ndarray]:

    if len(x) != len(y):
        raise ValueError("Количество x и y точек должно совпадать")
    if len(x) == 0:
        raise ValueError("Списки точек не могут быть пустыми")
    if len(x) == 1:
        raise ValueError("Для интерполяции нужно минимум 2 точки")
    if len(set(x)) != len(x):
        raise ValueError("x-координаты не должны повторяться")
    
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    x_new = np.asarray(x_new, dtype=np.float64)
    
    result = np.zeros_like(x_new)
    for i in range(len(x)):
        p = np.ones_like(x_new)
        for j in range(len(x)):
            if i != j:
                with np.errstate(divide='ignore', invalid='ignore'):
                    p *= (x_new - x[j]) / (x[i] - x[j])
        result += y[i] * p
    
    return result.item() if np.isscalar(x_new) else result