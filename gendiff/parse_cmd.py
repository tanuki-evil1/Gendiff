import argparse

PROGRAM = "gendiff"
DESCRIPTION = "Compares two configuration files and shows a difference."


def get_data_from_cmd() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=PROGRAM,
                                     description=DESCRIPTION)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish', help="set format of output")
    return parser.parse_args()
