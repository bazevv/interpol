import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from interpol.linear import linear_interpolation
from interpol.lagrange import lagrange_interpolation

def evaluate_interpolation():
    np.random.seed(0)
    x = np.linspace(0, 10, 20)
    y = np.sin(x) + 0.05 * np.random.randn(len(x))  # немного шума

    x_test = np.linspace(0, 10, 500)
    y_true = np.sin(x_test)

    results = {}

    methods = {
        "Linear": linear_interpolation,
        "Lagrange": lagrange_interpolation,
    }

    plt.figure(figsize=(10, 6))

    for name, method in methods.items():
        start = time.perf_counter()
        y_pred = method(x.tolist(), y.tolist(), x_test.tolist())
        elapsed = time.perf_counter() - start
        mse = mean_squared_error(y_true, y_pred)

        results[name] = {"mse": mse, "time": elapsed}
        plt.plot(x_test, y_pred, label=f"{name} (MSE={mse:.4f})")

    plt.plot(x_test, y_true, "k--", label="Ground truth: sin(x)")
    plt.scatter(x, y, color="r", s=10, label="Data")
    plt.title("Сравнение методов интерполяции")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/source/_static/performance_plot.png", dpi=300)

    return results