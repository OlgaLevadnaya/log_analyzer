import argparse
import json
from collections import defaultdict

from tabulate import tabulate


def send_report(cli_args: argparse.Namespace) -> None:
    """Формирует и выводит отчет в зависимости от выбранного типа."""
    report = cli_args.report
    files = cli_args.file

    if report == 'average':
        data = create_data(files)
        data = create_report_average(data)
        print_report(*data)
    else:
        print('Не выбран формат отчета')


def create_data(files: list) -> dict:
    """Парсит лог-файлы и создает словарь с временами ответов по URL."""
    result = defaultdict(list)
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                dict_obj = json.loads(line)
                result[dict_obj['url']].append(dict_obj['response_time'])

    return result


def create_report_average(result: dict) -> tuple[list, list]:
    """Считает среднее время ответа для каждого URL."""
    res_list = []
    for url, resp_time in sorted(result.items(), key=lambda x: -len(x[1])):
        res_list.append(
            [url, len(resp_time),  round(sum(resp_time) / len(resp_time), 3)])

    headers=['handler', 'total', 'avg_response_time']

    return (res_list, headers)


def print_report(res_list: list, headers: list) -> None:
    """Выводит данные в виде таблицы."""
    print(tabulate(res_list, headers=headers))
