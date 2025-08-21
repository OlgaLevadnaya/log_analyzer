import argparse


def configure_parser() -> argparse.ArgumentParser:
    """Создает и настраивает парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description='Скрипт для обработки лог-файлов')
    parser.add_argument(
        '-f',
        '--file',
        nargs='+',
        help='Путь к файлам',
    )
    parser.add_argument(
        '-r',
        '--report',
        choices=('average',),
        help='Название отчета',
    )

    return parser
