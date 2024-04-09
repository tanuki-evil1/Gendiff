import json


def json_formatter(diff_list: dict) -> str:
    return json.dumps(diff_list)
