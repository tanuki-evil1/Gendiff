from pathlib import Path
from gendiff.parse_files import get_files_data, get_yaml_items, get_json_items


def test_get_json_items():
    items = list(get_json_items(Path('tests/fixtures/file1.json')).items())
    expected = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    assert items == expected

    items = list(get_json_items(Path('tests/fixtures/file2.json')).items())
    expected = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    assert items == expected


def test_get_yaml_items():
    items = list(get_yaml_items(Path('tests/fixtures/file1.yml')).items())
    expected = [('host', 'hexlet.io'), ('timeout', 50), ('proxy', '123.234.53.22'), ('follow', False)]
    assert items == expected

    items = list(get_yaml_items(Path('tests/fixtures/file2.yaml')).items())
    expected = [('timeout', 20), ('verbose', True), ('host', 'hexlet.io')]
    assert items == expected


def test_get_files_data():
    expected = [{'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
                {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}]
    data = get_files_data('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert data == expected

    expected = [{'timeout': 20, 'verbose': True, 'host': 'hexlet.io'},
                {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}]
    data = get_files_data('tests/fixtures/file2.json', 'tests/fixtures/file1.json')
    assert data == expected
