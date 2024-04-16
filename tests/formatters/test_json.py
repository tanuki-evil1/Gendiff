import json
from gendiff.formatters.json import get_json_format


def test_json_formatter() -> None:
    result = get_json_format({'follow': ('-', False), 'host': 'hexlet.io', 'proxy': ('-', '123.234.53.22'),
                             'timeout': ('-+', (50, 20)), 'verbose': ('+', True)})
    expected = {'follow': ['-', False], 'host': 'hexlet.io', 'proxy': ['-', '123.234.53.22'],
                'timeout': ['-+', [50, 20]], 'verbose': ['+', True]}
    assert json.loads(result) == expected
