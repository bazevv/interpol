Примеры и Формулы
=================

📌 Этот раздел содержит формулы и примеры использования линейной и лагранжевой интерполяции.

Линейная интерполяция
----------------------

Формула линейной интерполяции между двумя точками:

.. math::

    L(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i} (x - x_i), \quad x \in [x_i, x_{i+1}]

Пример:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from interpol.linear import linear_interpolation

    x = np.array([0, 1, 2])
    y = np.array([0, 1, 4])
    x_new = np.linspace(0, 2, 100)
    y_new = linear_interpolation(x, y, x_new)

    plt.plot(x_new, y_new, label="Linear")
    plt.scatter(x, y, color="red")
    plt.legend()
    plt.grid()
    plt.show()

---

Полином Лагранжа
-----------------

Формула:

.. math::

    P(x) = \sum_{i=0}^{n} y_i \prod_{\substack{j=0 \\ j \ne i}}^{n} \frac{x - x_j}{x_i - x_j}

Пример:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from interpol.lagrange import lagrange_interpolation

    x = np.array([0, 1, 2])
    y = np.array([0, 1, 4])
    x_new = np.linspace(0, 2, 100)
    y_new = lagrange_interpolation(x, y, x_new)

    plt.plot(x_new, y_new, label="Lagrange")
    plt.scatter(x, y, color="red")
    plt.legend()
    plt.grid()
    plt.show()