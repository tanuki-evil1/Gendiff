import sys

from gendiff.diff import diff
from gendiff.parse_files import get_file_data
from gendiff.formatters import stylish, json, plain

FORMATTERS = {
    'stylish': stylish.stylish_formatter,
    'json': json.json_formatter,
    'plain': plain.plain_formatter
}


def generate_diff(file_path1: str, file_path2: str, form='stylish') -> str:
    try:
        dict1 = get_file_data(file_path1)
        dict2 = get_file_data(file_path2)
    except FileNotFoundError:
        print("Вы ввели неверный файл")
        sys.exit(1)
    diff_list = diff(dict1, dict2)
    return FORMATTERS[form](diff_list)
