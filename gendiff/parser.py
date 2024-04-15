import json
import yaml
from pathlib import Path
from typing import Dict, Any, AnyStr


def get_file_data(file_path: Path) -> AnyStr:
    return file_path.read_text()


def get_parse_data(data: AnyStr, form: str) -> Dict[str, Any]:
    try:
        if form == 'json':
            return json.loads(data)
        elif form == 'yaml' or form == 'yml':
            return yaml.load(data, Loader=yaml.Loader)
        else:
            raise ValueError('Invalid path')
    except (json.decoder.JSONDecodeError, yaml.YAMLError):
        raise SyntaxError
