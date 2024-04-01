from typing import Any


def normalize(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def plain_formatter(diff_list: dict) -> str:
    def walk(node: dict, accumulator='') -> list:  # TODO: узнать как давать тайпинг именованным аргументам
        styled = []

        for key, value in node.items():
            if isinstance(value, tuple):
                sign, value = value
                match sign:
                    case '+':
                        styled.append(f"Property '{accumulator}{key}' was added with value: {normalize(value)}")
                    case '-':
                        styled.append(f"Property '{accumulator}{key}' was removed")
                    case '-+':
                        styled.append(f"Property '{accumulator}{key}' was updated. From {normalize(value[0])} to {normalize(value[1])}")
            elif isinstance(value, dict):
                styled.extend(walk(value, accumulator + key + '.'))

        return styled
    return '\n'.join(walk(diff_list))
