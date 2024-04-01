def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def stylish_formatter(diff_list: dict) -> str:
    def walk(node, accumulator=1):
        styled = []
        for key, value in node.items():
            sign, value = value
            for index in range(
                    len(sign)):
                if len(sign) == 2:
                    if index > 0:
                        sub_value = normalize_value(value[1])
                    else:
                        sub_value = normalize_value(value[0])
                else:
                    sub_value = normalize_value(value)

                if isinstance(sub_value, dict):
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {key}: " + '{')
                    styled.append(walk(sub_value, accumulator + 1))
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}  " + '}')
                else:
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {key}: {sub_value}")

        return '\n'.join(styled)

    return '{\n' + walk(diff_list) + '\n}' if diff_list else '{}'
