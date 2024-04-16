import json


def get_json_format(diff_list: dict) -> str:
    return json.dumps(diff_list)
