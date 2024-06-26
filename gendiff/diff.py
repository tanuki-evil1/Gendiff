from typing import Any, Dict


def get_diff(data1: dict, data2: dict) -> Dict[str, Any]:
    result = {}
    sorted_keys = sorted((data1 | data2))
    for key in sorted_keys:
        if key not in data1:
            result[key] = 'added', data2[key]
        elif key not in data2:
            result[key] = 'removed', data1[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = 'nested', get_diff(data1[key], data2[key])
        elif data1[key] == data2[key]:
            result[key] = 'no_change', data1[key]
        elif data1[key] != data2[key]:
            result[key] = 'updated', (data1[key], data2[key])

    return result
