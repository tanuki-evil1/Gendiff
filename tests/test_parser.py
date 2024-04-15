import pytest
from pathlib import Path

from gendiff.parser import get_parse_data, get_file_data

FIXTURES_PATH = Path('tests/fixtures')


@pytest.mark.parametrize('path1, path2,', [('file3.json', 'file3.json'), ('file4.yaml', 'file4.yaml')])
def test_get_file_data(path1: Path, path2: Path) -> None:
    data = get_file_data(FIXTURES_PATH / path1)
    expected = (FIXTURES_PATH / path2).read_text()
    assert data == expected


@pytest.mark.parametrize('path1, path2,', [('file3.json', 'file3.yaml'), ('file4.json', 'file4.yaml')])
def test_get_parse_data(path1: Path, path2: Path) -> None:
    data1 = get_parse_data((FIXTURES_PATH / path1).read_text(), 'json')
    data2 = get_parse_data((FIXTURES_PATH / path1).read_text(), 'yaml')
    assert data1 == data2


def test_get_parse_data_errors() -> None:
    with pytest.raises(ValueError):
        get_parse_data('', '.err')

    with pytest.raises(SyntaxError):
        get_parse_data((FIXTURES_PATH / 'file0.json').read_text(), 'json')
