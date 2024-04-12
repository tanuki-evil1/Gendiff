from pathlib import Path

from gendiff.diff import diff
from gendiff.parser import get_file_data
from gendiff.formatters import stylish, json, plain

FORMATTERS = {
    'stylish': stylish.stylish_formatter,
    'json': json.json_formatter,
    'plain': plain.plain_formatter
}


def generate_diff(file_path1: str, file_path2: str, form='stylish') -> str:
    dict1 = get_file_data(Path(file_path1))
    dict2 = get_file_data(Path(file_path2))
    diff_list = diff(dict1, dict2)
    if not FORMATTERS.get(form, ''):
        raise ValueError('Wrong format. Use stylish, plain or json format')
    return FORMATTERS[form](diff_list)
