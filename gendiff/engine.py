from pathlib import Path

from gendiff.diff import get_diff
from gendiff.parser import get_parse_data, get_file_data
from gendiff.formatters import stylish, json, plain

FORMATTERS = {
    'stylish': stylish.get_stylish_format,
    'json': json.get_json_format,
    'plain': plain.get_plain_format
}


def get_format(path: Path):
    return path.suffix[1:]


def generate_diff(path1: str, path2: str, format_name='stylish') -> str:
    path1, path2 = Path(path1), Path(path2)

    form1, form2 = get_format(path1), get_format(path2)
    data1, data2 = get_file_data(path1), get_file_data(path2)

    dict1 = get_parse_data(data1, form1)
    dict2 = get_parse_data(data2, form2)

    diff_list = get_diff(dict1, dict2)
    if not FORMATTERS.get(format_name, ''):
        raise ValueError('Wrong format. Use stylish, plain or json format')
    return FORMATTERS[format_name](diff_list)
