from collections import defaultdict
from pathlib import Path

import pytest

try:
    from src import reports
except ModuleNotFoundError:
    assert False, 'В директории `src` отсутствует файл `reports.py`'
except ImportError:
    assert False, 'В директории `src` отсутствует файл `reports.py`'


@pytest.mark.parametrize('func', [
        'send_report', 'create_data', 'create_report_average', 'print_report',
])
def test_main_file(func: str) -> None:
    """Проверяет наличие необходимых функций в модуле reports.py."""
    assert hasattr(reports, func), (
        f'Отсутствует функция {func} в модуле `reports.py`.'
    )


def test_create_data(
    log_file: Path,
    response_time_data: dict,
    ) -> None:
    """Проверяет корректность создания словаря с данными о времени ответов."""
    actual = reports.create_data([str(log_file)])
    assert type(actual) is defaultdict
    assert actual == response_time_data


def test_create_report_average(
    response_time_data: dict,
    report_average_data: tuple[list, list],
    ) -> None:
    """Проверяет корректность формирования отчета
    со средним временем ответа.
    """
    actual = reports.create_report_average(response_time_data)
    assert (
        type(actual) is tuple and
        len(actual) == 2 and
        all(type(item) is list for item in actual)
    ), ('Функция `report_average` должна возвращать '
    'значение вида tuple[list, list]')
    assert actual == report_average_data


def test_print_report(
    report_average_data: tuple[list, list],
    output_data: str,
    capsys: pytest.CaptureFixture,
    ) -> None:
    """Проверяет корректность вывода отчета в консоль."""
    reports.print_report(*report_average_data)

    captured = capsys.readouterr()
    output = captured.out

    assert output == output_data
