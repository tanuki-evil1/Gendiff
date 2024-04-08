from gendiff.formatters.stylish import stylish_formatter


def test_stylish():
    with open('tests/fixtures/formatters/file_stylish_1_to_2.txt') as file:
        expected = file.read()

    dict1 = {'follow': ('removed', False), 'host': 'hexlet.io', 'proxy': ('removed', '123.234.53.22'),
             'timeout': ('updated', (50, 20)), 'verbose': ('added', True)}
    result = stylish_formatter(dict1)
    assert result == expected
