from pprint import pprint
from gendiff.parse_files import get_files_data  # TODO: Как организовывать нормальные импорты, если так то Pytest ругается
from gendiff.formatters.stylish import stylish_formatter


def diff(file1: dict, file2: dict) -> dict:
    result = {}

    # TODO: почему во время теста lint выводятся предупреждалки на lint
    def walk(file: dict):  # TODO: Надо ли мне это тестировать и другие моменты с pytes-cov
        if isinstance(file[key], dict):
            return diff(file[key], file[key])
        else:
            return file[key]

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


def generate_diff(file_path1: str, file_path2: str, form=stylish_formatter) -> str:
    dict1, dict2 = get_files_data(file_path1, file_path2)
    diff_list = diff(dict1, dict2)
    pprint(diff_list)
    return form(diff_list)
