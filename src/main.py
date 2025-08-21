import sys
from pathlib import Path

parent_dir =  Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from src.configs import configure_parser  # noqa: E402
from src.reports import send_report  # noqa: E402


def main() -> None:
    """Функция запуска приложения."""
    arg_parser = configure_parser()
    args = arg_parser.parse_args()
    send_report(args)


if __name__ == '__main__':
    main()
