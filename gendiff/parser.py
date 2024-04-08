import json
import yaml
from pathlib import Path
from typing import Dict, Any


def get_file_data(file_path: str) -> Dict[str, Any]:
    file_path = Path(file_path)
    with open(file_path) as file:
        if file_path.name.endswith('json'):
            return json.load(file)
        elif file_path.name.endswith(('yaml', 'yml')):
            return yaml.load(file, Loader=yaml.Loader)
