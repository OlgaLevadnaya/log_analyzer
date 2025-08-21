from pathlib import Path
from typing import Tuple

import pytest

current_dir =  Path(__file__).parent


@pytest.fixture
def log_file() -> Path:
    """Создает временный log-файл с тестовыми данными."""
    test_file = current_dir / "test.log"
    test_file.write_text(
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": '
        '"/api/context/...", "request_method": "GET", "response_time": 0.024, '
        '"http_user_agent": "..."}\n{"@timestamp": "2025-06-22T13:57:32+00:00'
        '", "status": 200, "url": "/api/context/...", "request_method": "GET",'
        ' "response_time": 0.02, "http_user_agent": "..."}\n{"@timestamp": '
        '"2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/..."'
        ', "request_method": "GET", "response_time": 0.024, "http_user_agent":'
        ' "..."}\n{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, '
        '"url": "/api/homeworks/...", "request_method": "GET", "response_time"'
        ': 0.06, "http_user_agent": "..."}\n{"@timestamp": "2025-06-22T13:57:'
        '32+00:00", "status": 200, "url": "/api/homeworks/...", "request_'
        'method": "GET", "response_time": 0.032, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": 0.06,'
        ' "http_user_agent": "..."}\n{"@timestamp": "2025-06-22T13:57:32+00:00'
        '", "status": 200, "url": "/api/homeworks/...", "request_method": '
        '"GET", "response_time": 0.06, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": 0.06,'
        ' "http_user_agent": "..."}\n{"@timestamp": "2025-06-22T13:57:32+00:00'
        '", "status": 200, "url": "/api/homeworks/...", "request_method": "GET'
        '", "response_time": 0.064, "http_user_agent": "..."}\n{"@timestamp": '
        '"2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/homeworks/'
        '...", "request_method": "GET", "response_time": 0.1, "http_user_agent'
        '": "..."}\n{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200,'
        ' "url": "/api/homeworks/...", "request_method": "GET", "response_time'
        '": 0.076, "http_user_agent": "..."}\n{"@timestamp": "2025-06-22T13:57'
        ':32+00:00", "status": 200, "url": "/api/homeworks/...", "request_'
        'method": "GET", "response_time": 0.076, "http_user_agent": "..."}',
        )
    return test_file


@pytest.fixture
def response_time_data() -> dict:
    """Создает тестовые данные, содержащие время ответов для эндпоинтов."""
    return {
        '/api/context/...': [0.024, 0.02, 0.024],
        '/api/homeworks/...': [0.06, 0.032, 0.06, 0.06, 0.06,
        0.064, 0.1, 0.076, 0.076],
        }


@pytest.fixture
def report_average_data() -> Tuple[list, list]:
    """Создает тестовые данные, содержащие количество запросов и
    среднее время ответов для эндпоинтов.
    """
    return ([
        ['/api/homeworks/...', 9, 0.065],
        ['/api/context/...', 3, 0.023]],
        ['handler', 'total', 'avg_response_time'])


@pytest.fixture
def output_data() -> str:
    """Создает тестовые данные для ожидаемого вывода."""
    return ('''handler               total    avg_response_time
------------------  -------  -------------------
/api/homeworks/...        9                0.065
/api/context/...          3                0.023
''')
