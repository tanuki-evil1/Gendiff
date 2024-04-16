import pytest

from gendiff.formatters.stylish import get_stylish_format


def test_stylish() -> None:
    with open('tests/fixtures/formatters/file_stylish_1_to_2.txt') as file:
        expected = file.read()

    dict1 = {'follow': ('removed', False), 'host': 'hexlet.io', 'proxy': ('removed', '123.234.53.22'),
             'timeout': ('updated', (50, 20)), 'verbose': ('added', True)}
    result = get_stylish_format(dict1)
    assert result == expected

    dict1 = {'follow': ('wrong', False)}
    with pytest.raises(ValueError):
        get_stylish_format(dict1)