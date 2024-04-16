#!/usr/bin/env python3
import sys

from gendiff.engine import generate_diff
from gendiff.cli import get_data_from_cmd


def main():
    args = get_data_from_cmd()
    file_path1 = args.first_file
    file_path2 = args.second_file
    form = args.format
    try:
        print(generate_diff(file_path1, file_path2, format_name=form))
    except OSError:
        print('System errors')
        sys.exit(1)
    except ValueError:
        print('Invalid path')
        sys.exit(1)
    except SyntaxError:
        print('Invalid format')
        sys.exit(1)


if __name__ == '__main__':
    main()
