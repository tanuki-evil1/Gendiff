from gendiff.formatters.plain import plain_formatter


def test_plain():
    with open('tests/fixtures/formatters/file_plain_3_to_4.txt') as file:
        expected = file.read()
    d = {'common': {'follow': ('added', False), 'setting1': 'Value 1', 'setting2': ('removed', 200),
                    'setting3': ('updated', (True, None)), 'setting4': ('added', 'blah blah'),
                    'setting5': ('added', {'key5': 'value5'}),
                    'setting6': {'doge': {'wow': ('updated', ('', 'so much'))}, 'key': 'value',
                                 'ops': ('added', 'vops')}},
         'group1': {'baz': ('updated', ('bas', 'bars')), 'foo': 'bar', 'nest': ('updated', ({'key': 'value'}, 'str'))},
         'group2': ('removed', {'abc': 12345, 'deep': {'id': 45}}),
         'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})}
    result = plain_formatter(d)
    assert result == expected

    with open('tests/fixtures/formatters/file_plain_1_to_2.txt') as file:
        expected = file.read()
    d = {'follow': ('removed', False), 'host': 'hexlet.io', 'proxy': ('removed', '123.234.53.22'),
         'timeout': ('updated', (50, 20)), 'verbose': ('added', True)}
    result = plain_formatter(d)
    assert result == expected
