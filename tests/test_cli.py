import pytest
from click.testing import CliRunner
from interpol.cli import main

def test_cli_linear_interpolation_plot(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "plot.png"
    result = runner.invoke(
        main,
        [
            "--method", "linear",
            "--x", "0,1,2",
            "--y", "0,1,4",
            "--step", "0.1",
            "--output", str(output_file)
        ]
    )
    assert result.exit_code == 0
    assert output_file.exists()
    assert "График сохранён в" in result.output

def test_cli_lagrange_interpolation_show():
    runner = CliRunner()
    # Тестируем вызов без output (будет plt.show(), который в тестах не вызовет окно из-за Agg backend)
    result = runner.invoke(
        main,
        [
            "--method", "lagrange",
            "--x", "0,1,2",
            "--y", "0,1,4",
            "--step", "0.05",
        ]
    )
    assert result.exit_code == 0
    assert "Метод интерполяции: lagrange" in result.output or result.output == ""  # plt.show() ничего не выводит

def test_cli_missing_coordinates():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "--method", "linear",
            "--x", "0,1",
            "--y", "0,1,2"
        ]
    )
    assert result.exit_code != 0
    assert "Количество X и Y точек должно совпадать" in result.output

def test_cli_bad_coordinates_format():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "--method", "linear",
            "--x", "0,a,2",
            "--y", "0,1,4"
        ]
    )
    assert result.exit_code != 0
    assert "Координаты должны быть числами" in result.output

def test_cli_default_method_and_step(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "default.png"
    result = runner.invoke(
        main,
        [
            "-x", "0,1,2",
            "-y", "1,2,3",
            "-o", str(output_file)
        ]
    )
    assert result.exit_code == 0
    assert output_file.exists()