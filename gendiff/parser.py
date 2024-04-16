import json
import yaml
from pathlib import Path
from typing import Dict, Any, AnyStr


def get_file_data(file_path: Path) -> AnyStr:
    return file_path.read_text()


def get_parse_data(data: AnyStr, format_name: str) -> Dict[str, Any]:
    try:
        if format_name == 'json':
            return json.loads(data)
        elif format_name == 'yaml' or format_name == 'yml':
            return yaml.load(data, Loader=yaml.Loader)
        else:
            raise ValueError('Invalid path')
    except (json.decoder.JSONDecodeError, yaml.YAMLError):
        raise SyntaxError('Invalid format')
