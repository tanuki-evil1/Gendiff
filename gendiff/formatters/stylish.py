from typing import Any
from itertools import chain

SIGNS = {
    'added': '+',
    'removed': '-',
    'updated': '-+',
    'no_change': ' ',
    'nested': ' ',
    '': ' '
}

INDENT = 4


def normalize(value: Any) -> Any:
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def get_line(key: str, value: Any, indent: str, sign: str = '') -> str:
    return f'{indent}{SIGNS[sign]} {key}: {value}'


def stylish_formatter(diff_list: dict, replacer: str = ' ') -> str:
    def get_lines(node: Any, depth: int = 0) -> str:
        if not isinstance(node, dict):
            return normalize(node)

        deep_indent_size = depth + INDENT
        deep_indent = deep_indent_size * replacer
        current_indent = depth * replacer
        lines = []
        for key, value in node.items():
            status = ''
            if isinstance(value, tuple):
                status, value = value

            if status == 'updated':
                lines.append(get_line(key,
                                      get_lines(value[0], deep_indent_size),
                                      deep_indent[:-2], 'removed'))
                lines.append(get_line(key,
                                      get_lines(value[1], deep_indent_size),
                                      deep_indent[:-2], 'added'))
            else:
                lines.append(get_line(key,
                                      get_lines(value, deep_indent_size),
                                      deep_indent[:-2], status))

        result = chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)

    return get_lines(diff_list)

#
