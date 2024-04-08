from typing import Any, Dict


def diff(data1: dict, data2: dict) -> Dict[str, Any]:
    result = {}

    def walk(file: dict) -> Any:
        if isinstance(file[key], dict):
            return diff(file[key], file[key])
        else:
            return file[key]

    for key in sorted((data1 | data2)):
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[key] = diff(data1[key], data2[key])
            else:
                if data1[key] == data2[key]:
                    result[key] = walk(data1)
                else:
                    result[key] = '-+', (walk(data1), walk(data2))
        elif key in data1:
            result[key] = '-', walk(data1)
        elif key in data2:
            result[key] = '+', walk(data2)
    return result
