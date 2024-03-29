def stylish(diff_list: dict) -> str:
    def walk(node, accumulator=1):
        styled = []
        for key, value in node.items():
            name, sign = key

            for index in range(len(sign)): # Из-за изменения структуры данных, пришлось ставить условие при котором sign
                if len(sign) == 2: # Может быть не только + или -, а еще и -+, обыграли циклом и создали условие, т.к
                    if index > 0: # значение теперь не только словарь или какой-то тип данных, но еще и кортеж с двумя
                        sub_value = value[1] # значениями, показалась более удобной из-за того, что не надо думать о сортировке значений одинаковых с + и - и также парсить их гораздо проще циклом
                    else:
                        sub_value = value[0]
                else:
                    sub_value = value

                if isinstance(sub_value, dict):
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {name}: " + '{')
                    styled.append(walk(sub_value, accumulator + 1))
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}  " + '}')
                else:
                    styled.append(f"{' ' * (4 * accumulator - len(sign[index]) - 1)}{sign[index]} {name}: {sub_value}")

        return '\n'.join(styled)

    return '{\n' + walk(diff_list) + '\n}' if diff_list else '{}'
