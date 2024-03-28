#!/usr/bin/env python3
from gendiff.engine import generate_diff
from gendiff.parse_cmd import get_data_from_cmd


def main():
    data = get_data_from_cmd()
    file_path1 = data.first_file
    file_path2 = data.second_file
    print(generate_diff(file_path1, file_path2))


if __name__ == '__main__':
    main()
