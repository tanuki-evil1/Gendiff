import json


def json_formatter(diff_list: dict) -> None:
    with open('result.json', 'w') as file:
        json.dump(diff_list, file, ensure_ascii=False, indent=4)
