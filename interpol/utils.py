import matplotlib.pyplot as plt


def plot_interpolation(x, y, x_new, y_new, title):
    plt.figure(figsize=(10, 5))
    plt.plot(x_new, y_new, "b-", label="Интерполяция")
    plt.scatter(x, y, color="r", label="Исходные точки")
    plt.title(title)
    plt.legend()
    plt.grid()
