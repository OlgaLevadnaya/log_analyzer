import pytest

   
try:
    from src import reports
except ModuleNotFoundError:
    assert False, 'В директории `src` отсутствует файл `reports.py`'
except ImportError:
    assert False, 'В директории `src` отсутствует файл `reports.py`'


def test_report_average()