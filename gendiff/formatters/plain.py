from typing import Any


# TODO: узнать как давать тайпинг именованным аргументам

def normalize(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def plain_formatter(diff_list: dict) -> str:
    def walk(node: dict, accum='') -> list:
        styled = []

        for key, value in node.items():
            if isinstance(value, tuple):
                sign, value = value
                match sign:
                    case '+':
                        val1 = normalize(value)
                        styled.append(f"Property '{accum}{key}'"
                                      f" was added with value: {val1}")
                    case '-':
                        styled.append(f"Property '{accum}{key}' was removed")
                    case '-+':
                        val1, val2 = normalize(value[0]), normalize(value[1])
                        styled.append(f"Property '{accum}{key}'"
                                      f" was updated. From {val1} to {val2}")
            elif isinstance(value, dict):
                styled.extend(walk(value, accum + key + '.'))

        return styled

    return '\n'.join(walk(diff_list))
