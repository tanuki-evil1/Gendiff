import pytest
from pathlib import Path

from gendiff.parser import get_file_data

FIXTURES_PATH = Path('tests/fixtures')


@pytest.mark.parametrize('path1, path2', [('file3.json', 'file3.yaml'), ('file4.json', 'file4.yml')])
def test_get_file_data(path1: Path, path2: Path) -> None:
    data1 = get_file_data(FIXTURES_PATH / path1)
    data2 = get_file_data(FIXTURES_PATH / path2)
    assert data1 == data2


def test_get_file_data_errors() -> None:
    with pytest.raises(ValueError):
        get_file_data(FIXTURES_PATH / '')

    with pytest.raises(SyntaxError):
        get_file_data(FIXTURES_PATH / 'file0.json')
