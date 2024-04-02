import pytest
from pathlib import Path

from gendiff.engine import diff, generate_diff

FIXTURES_PATH = Path('tests/fixtures')


def test_diff():
    expected = {'follow': ('-', False), 'host': 'hexlet.io', 'proxy': ('-', '123.234.53.22'),
                'timeout': ('-+', (50, 20)), 'verbose': ('+', True)}
    dict1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result = diff(dict1, dict2)
    assert result == expected


@pytest.mark.parametrize("path1, path2, res_path", [(f'{FIXTURES_PATH}/file1.json',
                                                     f'{FIXTURES_PATH}/file2.json',
                                                     f'{FIXTURES_PATH}/formatters/file_stylish_1_to_2.txt'),
                                                    (f'{FIXTURES_PATH}/file2.json',
                                                     f'{FIXTURES_PATH}/file1.json',
                                                     f'{FIXTURES_PATH}/formatters/file_stylish_2_to_1.txt'),
                                                    (f'{FIXTURES_PATH}/file1.yml',
                                                     f'{FIXTURES_PATH}/file2.yaml',
                                                     f'{FIXTURES_PATH}/formatters/file_stylish_1_to_2.txt'),
                                                    (f'{FIXTURES_PATH}/file2.yaml',
                                                     f'{FIXTURES_PATH}/file1.yml',
                                                     f'{FIXTURES_PATH}/formatters/file_stylish_2_to_1.txt'),
                                                    (f'{FIXTURES_PATH}/file3.yaml',
                                                     f'{FIXTURES_PATH}/file4.json',
                                                     f'{FIXTURES_PATH}/formatters/file_stylish_3_to_4.txt'),
                                                    ])
def test_generate_diff(path1, path2, res_path, form='stylish'):
    with open(res_path) as file:
        expected = file.read()
    result = generate_diff(path1, path2, form)
    assert result == expected
