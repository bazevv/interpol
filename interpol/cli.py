import click
import matplotlib.pyplot as plt
import numpy as np
from .lagrange import lagrange_interpolation
from .linear import linear_interpolation

def create_cli():
    @click.command()
    @click.option(
        "--method",
        type=click.Choice(["linear", "lagrange"], case_sensitive=False),
        default="linear",
        help="Метод интерполяции"
    )
    @click.option("--x", "-x", required=True, help="X-координаты через запятую", type=str)
    @click.option("--y", "-y", required=True, help="Y-координаты через запятую", type=str)
    @click.option("--step", type=float, default=0.1, help="Шаг интерполяции")
    @click.option("--output", "-o", type=click.Path(), help="Путь для сохранения графика")
    def cli_function(method, x, y, step, output):
        """Программа для интерполяции данных"""
        try:
            x_points = [float(num) for num in x.split(",")]
            y_points = [float(num) for num in y.split(",")]
        except ValueError:
            raise click.BadParameter("Координаты должны быть числами, разделенными запятыми")

        if len(x_points) != len(y_points):
            raise click.BadParameter("Количество X и Y точек должно совпадать")
        
        x_arr, y_arr = np.array(x_points), np.array(y_points)
        x_new = np.arange(min(x_arr), max(x_arr) + step, step)
        
        methods = {
            "linear": linear_interpolation,
            "lagrange": lagrange_interpolation
        }
        
        y_new = methods[method](x_arr, y_arr, x_new)
        
        plt.figure(figsize=(10, 5))
        plt.plot(x_new, y_new, "b-", label="Интерполяция")
        plt.scatter(x_arr, y_arr, color="r", label="Исходные точки")
        plt.title(f"{method} interpolation")
        plt.legend()
        plt.grid()

        if output:
            plt.savefig(output)
            click.echo(f"График сохранен в {output}")
        else:
            plt.show()
    
    return cli_function

main = create_cli()

if __name__ == "__main__":
    main()

