import pytest

def test_reports_import():    
    try:
        from src import reports
    except ModuleNotFoundError:
        assert False, 'Убедитесь что в директории `src` есть файл `reports.py`'
    except ImportError:
        assert False, 'Убедитесь что в директории `src` есть файл `reports.py`'