import os
import click
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from .lagrange import lagrange_interpolation
from .linear import linear_interpolation

# Установка бэкенда Matplotlib для тестов
if os.environ.get("TESTING", "0") == "1":
    matplotlib.use("Agg")

@click.command(help="""
Программа для интерполяции данных с возможностью визуализации.

Примеры использования:
\b
1. Линейная интерполяция:
   python -m interpol.cli -x 0,1,2 -y 0,1,4 --method linear -o plot.png
\b
2. Полином Лагранжа:
   python -m interpol.cli -x 0,1,2 -y 0,1,4 --method lagrange --step 0.01
\b
3. Минимальный пример:
   python -m interpol.cli -x 0,1 -y 0,1
""")
@click.option(
    "--method",
    type=click.Choice(["linear", "lagrange"], case_sensitive=False),
    default="linear",
    help="Метод интерполяции (linear или lagrange)",
)
@click.option(
    "--x", 
    "-x",
    required=True,
    help="X-координаты точек через запятую (например: 0,1,2)",
    type=str
)
@click.option(
    "--y",
    "-y",
    required=True,
    help="Y-координаты точек через запятую (например: 0,1,4)",
    type=str
)
@click.option(
    "--step",
    type=float,
    default=0.1,
    show_default=True,
    help="Шаг интерполяции между точками"
)
@click.option(
    "--output",
    "-o",
    type=click.Path(writable=True),
    default=None,
    help="Путь для сохранения графика (если не указан - показ в окне)"
)
def main(method, x, y, step, output):
    """Основная функция CLI для интерполяции данных"""
    try:
        # Преобразование входных данных
        x_points = [float(num) for num in x.split(",")]
        y_points = [float(num) for num in y.split(",")]
    except ValueError:
        raise click.BadParameter("Координаты должны быть числами, разделенными запятыми")

    if len(x_points) != len(y_points):
        raise click.BadParameter("Количество X и Y точек должно совпадать")

    x_arr = np.array(x_points, dtype=np.float64)
    y_arr = np.array(y_points, dtype=np.float64)
    x_new = np.arange(min(x_arr), max(x_arr) + step, step)

    # Выбор метода интерполяции
    methods = {
        "linear": linear_interpolation,
        "lagrange": lagrange_interpolation
    }
    
    y_new = methods[method](x_arr, y_arr, x_new)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x_new, y_new, "b-", label=f"{method} интерполяция")
    plt.scatter(x_arr, y_arr, color="r", label="Исходные точки")
    plt.title(f"Метод интерполяции: {method}")
    plt.legend()
    plt.grid(True)

    # Сохранение или показ графика
    if output:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        plt.savefig(output, dpi=300, bbox_inches="tight")
        click.echo(f"График сохранён в: {output}")
    else:
        plt.show()

if __name__ == "__main__":
    main()
