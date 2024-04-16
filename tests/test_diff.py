from gendiff.diff import get_diff


def test_diff() -> None:
    expected = {'follow': ('removed', False), 'host': ('no_change', 'hexlet.io'),
                'proxy': ('removed', '123.234.53.22'),
                'timeout': ('updated', (50, 20)), 'verbose': ('added', True)}

    dict1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result = get_diff(dict1, dict2)
    assert result == expected
