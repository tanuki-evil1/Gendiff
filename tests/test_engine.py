from gendiff import engine


def test_diff():
    expected = {('follow', '-'): 'false', ('host', ' '): 'hexlet.io', ('proxy', '-'): '123.234.53.22',
                ('timeout', '-'): '50', ('timeout', '+'): '20', ('verbose', '+'): 'true'}
    dict1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result = engine.diff(dict1, dict2)
    assert result == expected


def test_generate_diff():
    with open('tests/fixtures/engine/generate_diff/file_stylish_1_to_2.txt') as file:
        expected = file.read()
    result = engine.generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == expected

    with open('tests/fixtures/engine/generate_diff/file_stylish_2_to_1.txt') as file:
        expected = file.read()
    result = engine.generate_diff('tests/fixtures/file2.json', 'tests/fixtures/file1.json')
    assert result == expected

    with open('tests/fixtures/engine/generate_diff/file_stylish_1_to_2.txt') as file:
        expected = file.read()
    result = engine.generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml')
    assert result == expected

    with open('tests/fixtures/engine/generate_diff/file_stylish_2_to_1.txt') as file:
        expected = file.read()
    result = engine.generate_diff('tests/fixtures/file2.yaml', 'tests/fixtures/file1.yml')
    assert result == expected

    result = engine.generate_diff('tests/fixtures/file0.json', 'tests/fixtures/file0.json')
    assert result == '{}'

    # result = engine.generate_diff('tests/fixtures/engine/file3.json', 'tests/fixtures/engine/file4.json')
    # with open('tests/fixtures/engine/generate_diff/result_3_to_4.txt', 'w') as file:
    #     file.write(result)
    #
    # path1 = 'tests/fixtures/engine/generate_diff/file_stylish_3_to_4.txt'
    # path2 = 'tests/fixtures/engine/generate_diff/result_3_to_4.txt'
    # with open(path1) as file1, open(path2) as file2:
    #     expected = file1.readlines()
    #     result = file2.readlines()
    #
    # assert  result == expected
