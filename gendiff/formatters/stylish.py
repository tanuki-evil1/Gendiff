from typing import Any


def normalize(value: Any) -> Any:
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def stylish_formatter(diff_list: dict) -> str: # TODO: Попробовать переписать
    def walk(node, accumulator=1) -> list:
        styled = []
        for key, value in node.items():
            if isinstance(value, tuple):
                sign, value = value
            else:
                sign = ' '
            for index in range(len(sign)):
                if len(sign) == 2:
                    if index > 0:
                        sub_value = normalize(value[1])
                    else:
                        sub_value = normalize(value[0])
                else:
                    sub_value = normalize(value)

                if isinstance(sub_value, dict):
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {key}: " + '{')
                    styled.extend(walk(sub_value, accumulator + 1))
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}  " + '}')
                else:
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {key}: {sub_value}")

        return styled
    return '{\n' + '\n'.join(walk(diff_list)) + '\n}' if diff_list else '{}'
