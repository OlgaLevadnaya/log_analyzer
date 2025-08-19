import sys
from pathlib import Path

parent_dir =  Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from src.configs import configure_parser
from src.reports import send_report


def main():
    arg_parser = configure_parser()
    args = arg_parser.parse_args()
    send_report(args)


if __name__ == '__main__':
    main()
