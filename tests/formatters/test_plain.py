from gendiff.formatters.plain import plain_formatter


def test_plain():
    with open('tests/fixtures/formatters/file_plain_3_to_4.txt') as file:
        expected = file.read()

    dict1 = {'common': {'follow': ('+', False), 'setting1': 'Value 1', 'setting2': ('-', 200),
                        'setting3': ('-+', (True, None)), 'setting4': ('+', 'blah blah'),
                        'setting5': ('+', {'key5': 'value5'}),
                        'setting6': {'doge': {'wow': ('-+', ('', 'so much'))}, 'key': 'value', 'ops': ('+', 'vops')}},
             'group1': {'baz': ('-+', ('bas', 'bars')), 'foo': 'bar', 'nest': ('-+', ({'key': 'value'}, 'str'))},
             'group2': ('-', {'abc': 12345, 'deep': {'id': 45}}),
             'group3': ('+', {'deep': {'id': {'number': 45}}, 'fee': 100500})}

    result = plain_formatter(dict1)
    assert result == expected
