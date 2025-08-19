from collections import defaultdict
import json
from tabulate import tabulate


def send_report(cli_args):
    report = cli_args.report
    files = cli_args.file

    if report == 'average':
        print_report(*report_average(files))        
    else:
        print('Не выбран формат отчета')

def report_average(files):
    result = defaultdict(list)
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                dict_obj = json.loads(line)
                result[dict_obj['url']].append(dict_obj['response_time'])
    
    res_list = []
    for url, resp_time in sorted(result.items(), key=lambda x: -len(x[1])):
        res_list.append([url, len(resp_time),  round(sum(resp_time) / len(resp_time), 3)])

    headers=['handler', 'total', 'avg_response_time']

    return (res_list, headers)


def print_report(res_list, headers):
    print(tabulate(res_list, headers=headers))
