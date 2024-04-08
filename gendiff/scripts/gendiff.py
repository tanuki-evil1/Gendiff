#!/usr/bin/env python3
import sys

from gendiff.engine import generate_diff
from gendiff.cli import get_data_from_cmd


def main():
    data = get_data_from_cmd()
    file_path1 = data.first_file
    file_path2 = data.second_file
    form = data.format

    try:
        print(generate_diff(file_path1, file_path2, form=form))
    except FileNotFoundError:
        print("Вы ввели неверный путь")
        sys.exit(1)


if __name__ == '__main__':
    main()
