from typing import Any


def normalize(value: Any) -> Any:
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, str):
        result = f"'{value}'"
    else:
        result = value
    return result


def bypass_nested(node: dict, accum: str = '') -> list:
    styled = []
    for key, value in node.items():
        sign, value = value
        match sign:
            case 'added':
                val1 = normalize(value)
                styled.append(f"Property '{accum}{key}'"
                              f" was added with value: {val1}")
            case 'removed':
                styled.append(f"Property '{accum}{key}' was removed")
            case 'updated':
                val1, val2 = normalize(value[0]), normalize(value[1])
                styled.append(f"Property '{accum}{key}'"
                              f" was updated. From {val1} to {val2}")
            case 'nested':
                styled.extend(bypass_nested(value, accum + key + '.'))
            case 'no_change':
                pass
            case _:
                raise ValueError('Invalid data')
    return styled


def get_plain_format(diff_list: dict) -> str:
    return '\n'.join(bypass_nested(diff_list))
