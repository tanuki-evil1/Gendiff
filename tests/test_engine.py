import pytest
from pathlib import Path

from gendiff.engine import generate_diff

FIXTURES_PATH = Path('tests/fixtures')


@pytest.mark.parametrize("path1, path2, res_path", [('file1.json',
                                                     'file2.json',
                                                     'formatters/file_stylish_1_to_2.txt'),
                                                    ('file2.json',
                                                     'file1.json',
                                                     'formatters/file_stylish_2_to_1.txt'),
                                                    ('file3.yaml',
                                                     'file4.json',
                                                     'formatters/file_stylish_3_to_4.txt'),
                                                    ])
def test_generate_diff(path1: str, path2: str, res_path: str) -> None:
    with open(FIXTURES_PATH / res_path) as file:
        expected = file.read()

    path1 = FIXTURES_PATH / path1
    path2 = FIXTURES_PATH / path2
    result = generate_diff(str(path1), str(path2))
    assert result == expected


@pytest.mark.parametrize("path1, path2, error", [('file1.json',
                                                  'file2.json',
                                                  ValueError)])
def test_generate_diff_errors(path1: str, path2: str, error):
    path1 = FIXTURES_PATH / path1
    path2 = FIXTURES_PATH / path2
    with pytest.raises(error):
        generate_diff(str(path1), str(path2), '')

