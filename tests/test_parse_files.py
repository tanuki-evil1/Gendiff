import pytest
from pathlib import Path

from gendiff.parser import get_file_data

FIXTURES_PATH = Path('tests/fixtures')


@pytest.mark.parametrize('path, expected', [
    ('file1.json', {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}),
    ('file2.json', {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'})])
def test_get_file_data(path, expected):
    data = get_file_data(FIXTURES_PATH / path)
    assert data == expected
