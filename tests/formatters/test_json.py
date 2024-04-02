import os.path
from gendiff.formatters.json import json_formatter


def test_json_formatter():
    json_formatter({'follow': ('-', False), 'host': 'hexlet.io', 'proxy': ('-', '123.234.53.22'),
                    'timeout': ('-+', (50, 20)), 'verbose': ('+', True)})
    assert os.path.isfile('result.json')
    os.remove("result.json")
