from pathlib import Path
from gendiff.parse_files import get_files_data, get_yaml_items, get_json_items

FIXTURES_PATH = Path('tests/fixtures')


def test_get_json_items():
    items = list(get_json_items(FIXTURES_PATH / 'file1.json').items())
    expected = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    assert items == expected

    items = list(get_json_items(FIXTURES_PATH / 'file2.json').items())
    expected = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    assert items == expected


def test_get_yaml_items():
    items = list(get_yaml_items(FIXTURES_PATH / 'file1.yml').items())
    expected = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    assert items == expected

    items = list(get_yaml_items(FIXTURES_PATH / 'file2.yaml').items())
    expected = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    assert items == expected


def test_get_files_data():
    data = get_files_data(f'{FIXTURES_PATH}/file1.json', f'{FIXTURES_PATH}/file2.json')
    expected = [{'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
                {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}]
    assert data == expected

    data = get_files_data(f'{FIXTURES_PATH}/file2.json', f'{FIXTURES_PATH}/file1.json')
    expected = [{'timeout': 20, 'verbose': True, 'host': 'hexlet.io'},
                {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}]
    assert data == expected
