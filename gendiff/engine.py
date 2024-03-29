from pprint import pprint
from typing import Any
from parse_files import get_files_data # Как организовывать нормальные импорты, если так то Pytest ругается
from formatters.stylish import stylish
from formatters.plain import plain


def normalize_data(item: Any) -> str:
    if isinstance(item, bool):
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return str(item)


def diff(file1: dict, file2: dict) -> dict:
    result = {}

    def walk(file: dict):  # TODO: Надо ли мне эт   о тестировать и другие моменты с coverage
        if isinstance(file[key], dict):
            return diff(file[key], file[key])
        else:
            return normalize_data(file[key])

    for key in sorted((file1 | file2)):
        if key in file1 and key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                result[key, ' '] = diff(file1[key], file2[key])
            else:
                if file1[key] == file2[key]:
                    result[key, ' '] = walk(file1)
                else:
                    result[key, '-+'] = walk(file1), walk(file2)
        elif key in file1:
            result[key, '-'] = walk(file1)
        elif key in file2:
            result[key, '+'] = walk(file2)
    return result


def generate_diff(file_path1: str, file_path2: str, form=stylish) -> str:
    dict1, dict2 = get_files_data(file_path1, file_path2)
    diff_list = diff(dict1, dict2)
    pprint(diff_list)
    return form(diff_list)

print(generate_diff('../tests/fixtures/file3.json', '../tests/fixtures/file4.json'))