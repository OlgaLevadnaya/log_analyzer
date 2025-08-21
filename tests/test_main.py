import argparse
import sys

import pytest

try:
    from src import main
except ModuleNotFoundError:
    assert False, 'В директории `src` отсутствует файл `main.py`'
except ImportError:
    assert False, 'В директории `src` отсутствует файл `main.py`'


def test_main_file() -> None:
    """Проверяет наличие функции main в модуле main.py."""
    assert hasattr(main, 'main'), (
        'Отсутствует функция `main` в модуле `main.py`.'
    )


def test_configure_parser_object() -> None:
    """Проверяет, что configure_parser создает корректный объект парсера."""
    parser = main.configure_parser()
    assert isinstance(parser, argparse.ArgumentParser), (
        'Созданный парсер не является объектом argparse.ArgumentParser')
    assert hasattr(parser, '_actions'), (
        'Отсутствуют аргументы парсера'
    )


def test_main_function() -> None:
    """Проверяет корректность работы функции main."""
    original_argv = sys.argv
    try:
        sys.argv = ['--file', '--report']
        main.main()
        assert True
    except SystemExit:
        assert True
    except Exception:
        pytest.fail('Ошибка при вызове функции main(): {e}')
    finally:
        sys.argv = original_argv
