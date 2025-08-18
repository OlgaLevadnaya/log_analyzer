from configs import configure_parser

from reports import send_report


def main():
    arg_parser = configure_parser()
    args = arg_parser.parse_args()
    send_report(args)


if __name__ == '__main__':
    main()
    