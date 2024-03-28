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
