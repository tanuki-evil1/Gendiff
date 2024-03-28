import json
import yaml
from pathlib import Path
from typing import Dict, Any


def get_json_items(file_path: Path) -> Dict[str, Any]:
    with open(file_path) as file1:
        return json.load(file1)


def get_yaml_items(file_path: Path) -> Dict[str, Any]:
    with open(file_path) as file1:
        return yaml.load(file1, Loader=yaml.Loader)


def get_files_data(file_path1: str, file_path2: str) -> list:
    data = []
    for path in [Path(file_path1), Path(file_path2)]:
        if path.name.endswith('.yaml') or path.name.endswith('.yml'):
            data.append(get_yaml_items(path))
        elif path.name.endswith('.json'):
            data.append(get_json_items(path))
    return data
