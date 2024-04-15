from pathlib import Path

from gendiff.diff import diff
from gendiff.parser import get_parse_data, get_file_data
from gendiff.formatters import stylish, json, plain

FORMATTERS = {
    'stylish': stylish.stylish_formatter,
    'json': json.json_formatter,
    'plain': plain.plain_formatter
}


def generate_diff(path1: str, path2: str, form='stylish') -> str:
    path1, path2 = Path(path1), Path(path2)
    form1, form2 = path1.suffix[1:], path2.suffix[1:]
    data1, data2 = get_file_data(path1), get_file_data(path2)

    dict1 = get_parse_data(data1, form1)
    dict2 = get_parse_data(data2, form2)
    diff_list = diff(dict1, dict2)
    if not FORMATTERS.get(form, ''):
        raise ValueError('Wrong format. Use stylish, plain or json format')
    return FORMATTERS[form](diff_list)
