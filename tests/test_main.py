import pytest

def test_main_import():    
    try:
        from src import main
    except ModuleNotFoundError:
        assert False, 'Убедитесь что в директории `src` есть файл `main.py`'
    except ImportError:
        assert False, 'Убедитесь что в директории `src` есть файл `main.py`'

