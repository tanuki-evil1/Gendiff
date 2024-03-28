def plain(diff_list: dict) -> str: # TODO: Доделать плейн
    def walk(node, accumulator=''):
        styled = []
        for key, value in node.items():
            name, sign = key

            if isinstance(value, dict):
                styled.append(walk(value, accumulator + name))
            else:
                if sign == '+':
                    styled.append(f"Property '{accumulator}.{name}' was added with value: {value}")
                elif sign == '-':
                    styled.append(f"Property '{accumulator}.{name}' was removed")

        return '\n'.join(styled)

    return '{\n' + walk(diff_list) + '\n}' if diff_list else '{}'
