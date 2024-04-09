import pytest
from pathlib import Path

from gendiff.engine import generate_diff

FIXTURES_PATH = Path('tests/fixtures')


# Убрать дубликат Fixture_path и тесты с yaml
@pytest.mark.parametrize("path1, path2, res_path", [('file1.json',
                                                     f'file2.json',
                                                     f'formatters/file_stylish_1_to_2.txt'),
                                                    (f'file2.json',
                                                     f'file1.json',
                                                     f'formatters/file_stylish_2_to_1.txt'),
                                                    (f'file1.yml',
                                                     f'file2.yaml',
                                                     f'formatters/file_stylish_1_to_2.txt'),
                                                    (f'file2.yaml',
                                                     f'file1.yml',
                                                     f'formatters/file_stylish_2_to_1.txt'),
                                                    (f'file3.yaml',
                                                     f'file4.json',
                                                     f'formatters/file_stylish_3_to_4.txt'),
                                                    ])
def test_generate_diff(path1, path2, res_path, form='stylish'):
    with open(FIXTURES_PATH / res_path) as file:
        expected = file.read()
    path1 = f'{FIXTURES_PATH}/{path1}'
    path2 = f'{FIXTURES_PATH}/{path2}'
    result = generate_diff(path1, path2, form)
    assert result == expected
