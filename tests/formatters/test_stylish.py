from gendiff.formatters.stylish import stylish


def test_stylish():
    with open('tests/fixtures/engine/generate_diff/file_stylish_1_to_2.txt') as file:
        expected = file.read()
    dict1 = {('follow', '-'): 'false', ('host', ' '): 'hexlet.io', ('proxy', '-'): '123.234.53.22',
             ('timeout', '-'): '50', ('timeout', '+'): '20', ('verbose', '+'): 'true'}
    result = stylish(dict1)
    assert result == expected
