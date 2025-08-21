import argparse
from typing import Optional

import pytest

try:
    from src import configs as configs
except ModuleNotFoundError:
    assert False, 'В директории `src` отсутствует файл `configs.py`'
except ImportError:
    assert False, 'В директории `src` отсутствует файл `configs.py`'


def test_configs_file() -> None:
    """Проверяет наличие функции configure_parser в модуле configs."""
    assert hasattr(configs, 'configure_parser'), (
        'Отсутствует функция `configure_parser` в модуле `configs.py`.'
    )


@pytest.mark.parametrize('action, option_string, dest, choices', [
    (
        argparse._StoreAction, ['-f', '--file'], 'file', None,
    ),
    (
        argparse._StoreAction, ['-r', '--report'], 'report', ('average',),
    ),
])
def test_configure_parser(
    action: type[argparse.Action],
    option_string: list[str],
    dest: str,
    choices: Optional[tuple[str, ...]],
    ) -> None:
    """Проверяет настройки парсера аргументов командной строки."""
    actual = configs.configure_parser()
    actual_actions = [
        act for act in actual._actions
        if isinstance(act, action) and act.dest == dest
    ]
    if not actual_actions:
        assert False, (f'Cli аргумент {dest} не отсутствует')

    actual_action = actual_actions[0]
    assert isinstance(actual_action, action)
    assert actual_action.option_strings == option_string, (
        f'Неверный флаг для аргумента {actual_action.dest}')
    assert actual_action.dest == dest, (
        f'Неверное имя для аргумента {actual_action.dest}')
    assert actual_action.choices == choices, (
        f'Неверный выбор для аргумента {actual_action.dest}')
