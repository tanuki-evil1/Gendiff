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
REPLACER = ' '


def normalize(value: Any) -> Any:
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def get_line(key: str, value: Any, indent: str, sign: str = '') -> str:
    return f'{indent}{SIGNS[sign]} {key}: {value}'


def get_indents(depth):
    deep_indent_size = depth + INDENT
    deep_indent = deep_indent_size * REPLACER
    current_indent = depth * REPLACER
    return deep_indent_size, deep_indent, current_indent


def bypass_nested(node: Any, depth: int = 0) -> str:
    if not isinstance(node, dict):
        return normalize(node)

    deep_indent_size, deep_indent, current_indent = get_indents(depth)
    lines = []
    for key, value in node.items():
        status = ''
        if isinstance(value, tuple):
            status, value = value

        if status == 'updated':
            lines.append(get_line(key,
                                  bypass_nested(value[0], deep_indent_size),
                                  deep_indent[:-2], 'removed'))
            lines.append(get_line(key,
                                  bypass_nested(value[1], deep_indent_size),
                                  deep_indent[:-2], 'added'))
        elif status in ['added', 'removed', 'no_change', 'nested', '']:
            lines.append(get_line(key,
                                  bypass_nested(value, deep_indent_size),
                                  deep_indent[:-2], status))

    result = chain('{', lines, [current_indent + '}'])
    return '\n'.join(result)


def get_stylish_format(diff_list: dict) -> str:
    return bypass_nested(diff_list)
