#!/usr/bin/env python3
from gendiff.engine import generate_diff
from gendiff.parse_cmd import get_data_from_cmd
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.stylish import stylish_formatter

formatters = {
    'plain': plain_formatter,
    'stylish': stylish_formatter
}


def main():
    data = get_data_from_cmd()
    file_path1 = data.first_file
    file_path2 = data.second_file
    form = formatters[data.format]
    print(generate_diff(file_path1, file_path2, form=form))


if __name__ == '__main__':
    main()
