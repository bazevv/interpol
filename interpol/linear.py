import numpy as np
from typing import List, Union

def linear_interpolation(
    x: List[float], 
    y: List[float], 
    x_new: Union[float, List[float]]
) -> Union[float, np.ndarray]:

    if len(x) != len(y):
        raise ValueError("Количество x и y точек должно совпадать")
    if len(x) < 2:
        raise ValueError("Для интерполяции нужно минимум 2 точки")
    
    return np.interp(x_new, x, y)