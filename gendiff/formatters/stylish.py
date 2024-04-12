from typing import Any
from itertools import chain

SIGNS = {
    'added': '+',
    'removed': '-',
    'updated': '-+',
    'nested': ' ',
    'no_change': ' ',
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


def stylish_formatter(diff_list: dict, replacer=' '):
    def walk(node, depth: int = 0):
        if not isinstance(node, dict):
            return normalize(node)

        deep_indent_size = depth + INDENT
        deep_indent = deep_indent_size * replacer
        current_indent = depth * replacer
        lines = []
        for key, value in node.items():
            sign = ''
            if isinstance(value, tuple):
                sign, value = value
                if sign == 'updated':
                    lines.append(f'{deep_indent[:-2]}{SIGNS[sign][0]} {key}: {walk(value[0], deep_indent_size)}')
                    lines.append(f'{deep_indent[:-2]}{SIGNS[sign][1]} {key}: {walk(value[1], deep_indent_size)}')
                    continue

            lines.append(f'{deep_indent[:-2]}{SIGNS[sign]} {key}: {walk(value, deep_indent_size)}')
        result = chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)

    return walk(diff_list)
