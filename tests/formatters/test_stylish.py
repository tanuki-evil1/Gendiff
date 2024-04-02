from gendiff.formatters.stylish import stylish_formatter


def test_stylish():
    with open('tests/fixtures/formatters/file_stylish_1_to_2.txt') as file:
        expected = file.read()

    dict1 = {'follow': ('-', False), 'host': 'hexlet.io', 'proxy': ('-', '123.234.53.22'),
             'timeout': ('-+', (50, 20)), 'verbose': ('+', True)}
    result = stylish_formatter(dict1)
    assert result == expected
