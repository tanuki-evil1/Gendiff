import json
import yaml
from pathlib import Path
from typing import Dict, Any


def get_json(file_path: Path) -> Dict[str, Any]:
    with open(file_path) as file:
        return json.load(file)


def get_yaml(file_path: Path) -> Dict[str, Any]:
    with open(file_path) as file:
        return yaml.load(file, Loader=yaml.Loader)


def get_file_data(file_path: Path) -> Dict[str, Any]:
    try:
        if file_path.name.endswith('json'):
            return get_json(file_path)
        elif file_path.name.endswith(('yaml', 'yml')):
            return get_yaml(file_path)
        else:
            raise ValueError('Invalid path to the json or yaml file')
    except (json.decoder.JSONDecodeError, yaml.YAMLError):
        raise SyntaxError
