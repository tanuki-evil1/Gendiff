from typing import Any
from gendiff.parse_files import get_files_data


def normalize_data(item: Any) -> str:
    if isinstance(item, bool):
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return str(item)


def diff(file1: dict, file2: dict) -> dict:
    result = {}

    def walk(file: dict):  # TODO: Надо ли мне это тестировать и другие моменты с coverage
        if isinstance(file[key], dict):
            return diff(file[key], file[key])
        else:
            return normalize_data(file[key])

    for key in sorted((file1 | file2)):
        if key in file1 and key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                result[key, ' '] = diff(file1[key], file2[key])
            else:
                if file1[key] == file2[key]:
                    result[key, ' '] = walk(file1)
                else:
                    result[key, '-'] = walk(file1)
                    result[key, '+'] = walk(file2)
        elif key in file1:
            result[key, '-'] = walk(file1)
        elif key in file2:
            result[key, '+'] = walk(file2)
    return result


def stylish(diff_list: dict) -> str:
    def walk(node, accumulator=1):
        styled = []
        for key, value in node.items():
            name, sign = key

            if isinstance(value, dict):
                styled.append(f"{' ' * (4 * accumulator - len(sign) - 1)}{sign} {name}: " + '{')
                styled.append(walk(value, accumulator + 1))
                styled.append(f"{' ' * (4 * accumulator - len(sign) - 1)}  " + '}')
            else:
                styled.append(f"{' ' * (4 * accumulator - len(sign) - 1)}{sign} {name}: {value}")

        return '\n'.join(styled)
    return '{\n' + walk(diff_list) + '\n}' if diff_list else '{}'


def generate_diff(file_path1: str, file_path2: str) -> str:
    dict1, dict2 = get_files_data(file_path1, file_path2)
    diff_list = diff(dict1, dict2)
    return stylish(diff_list)
