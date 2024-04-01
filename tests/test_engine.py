from pathlib import Path

from gendiff.engine import diff, generate_diff

FIXTURE_PATH = Path(__file__).parent / 'fixtures'


def test_diff():
    expected = {('follow', '-'): 'false', ('host', ' '): 'hexlet.io', ('proxy', '-'): '123.234.53.22',
                ('timeout', '-'): '50', ('timeout', '+'): '20', ('verbose', '+'): 'true'}
    dict1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result = diff(dict1, dict2)
    assert result == expected


# TODO: Не хардкодить пути к фикстурам
# TODO: Поискать про PythonPath в pytest или еще где-то
def test_generate_diff():
    with open(f'{FIXTURE_PATH}/formatters/file_stylish_1_to_2.txt') as file:
        expected = file.read()
    result = generate_diff(f'{FIXTURE_PATH}/file1.json', f'{FIXTURE_PATH}/file2.json')
    assert result == expected

    with open(f'{FIXTURE_PATH}/formatters/file_stylish_2_to_1.txt') as file:
        expected = file.read()
    result = generate_diff(f'{FIXTURE_PATH}/file2.json', f'{FIXTURE_PATH}/file1.json')
    assert result == expected

    with open(f'{FIXTURE_PATH}/formatters/file_stylish_1_to_2.txt') as file:
        expected = file.read()
    result = generate_diff(f'{FIXTURE_PATH}/file1.yml', f'{FIXTURE_PATH}/file2.yaml')
    assert result == expected

    with open(f'{FIXTURE_PATH}/formatters/file_stylish_2_to_1.txt') as file:
        expected = file.read()
    result = generate_diff(f'{FIXTURE_PATH}/file2.yaml', f'{FIXTURE_PATH}/file1.yml')
    assert result == expected

    result = generate_diff(f'{FIXTURE_PATH}/file0.json', f'{FIXTURE_PATH}/file0.json')
    assert result == '{}'

    # result = generate_diff(f'{FIXTURE_PATH}/file3.json', f'{FIXTURE_PATH}/file4.json')
    # with open(f'{FIXTURE_PATH}/formatters/result_3_to_4.txt', 'w') as file:
    #     file.write(result)
    # TODO: Потестировать вывод
    # path1 = f'{FIXTURE_PATH}/formatters/file_stylish_3_to_4.txt'
    # path2 = f'{FIXTURE_PATH}/formatters/result_3_to_4.txt'
    # with open(path1) as file1, open(path2) as file2:
    #     expected = file1.readlines()
    #     result = file2.readlines()
    #
    # assert  result == expected
