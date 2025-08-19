import pytest

def test_configs_import():    
    try:
        from src import configs
    except ModuleNotFoundError:
        assert False, 'Убедитесь что в директории `src` есть файл `configs.py`'
    except ImportError:
        assert False, 'Убедитесь что в директории `src` есть файл `configs.py`'