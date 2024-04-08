from pathlib import Path
from gendiff.parse_files import get_file_data

FIXTURES_PATH = Path('tests/fixtures')


def test_get_file_data():
    data = get_file_data(f'{FIXTURES_PATH}/file1.json')
    expected = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert data == expected

    data = get_file_data(f'{FIXTURES_PATH}/file2.json')
    expected = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert data == expected
