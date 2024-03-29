from gendiff.formatters.plain import plain_formatter


def test_plain():
    with open('tests/fixtures/engine/generate_diff/file_plain_1_to_2.txt') as file:
        expected = file.read()
    dict1 = {('follow', '-'): 'false', ('host', ' '): 'hexlet.io', ('proxy', '-'): '123.234.53.22',
             ('timeout', '-'): '50', ('timeout', '+'): '20', ('verbose', '+'): 'true'}
    result = plain_formatter(dict1)
    assert result == expected
