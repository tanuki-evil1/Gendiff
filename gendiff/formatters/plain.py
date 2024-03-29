def normalize(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def plain_formatter(diff_list: dict) -> str:
    def walk(node, accumulator=''):
        styled = []
        for key, value in node.items():
            name, sign = key
            match sign:
                case '+':
                    styled.append(f"Property '{accumulator}{name}' was added with value: {normalize(value)}")
                case '-':
                    styled.append(f"Property '{accumulator}{name}' was removed")
                case '-+':
                    styled.append(f"Property '{accumulator}{name}' was updated. "
                                  f"From {normalize(value[0])} to {normalize(value[1])}")
                case ' ':
                    if isinstance(value, dict):
                        styled.append(walk(value, accumulator + name + '.'))

        return '\n'.join(styled)

    return walk(diff_list)
