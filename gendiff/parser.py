import json
import yaml
import sys
from pathlib import Path
from typing import Dict, Any


def get_file_data(file_path: Path) -> Dict[str, Any]:
    try:
        with open(file_path) as file:
            if file_path.name.endswith('json'):
                return json.load(file)
            elif file_path.name.endswith(('yaml', 'yml')):
                return yaml.load(file, Loader=yaml.Loader)
    # TODO: Как запускать ошибки и отлавливать их в тестах
    except FileNotFoundError:
        print('File not found.')
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print('Incorrect JSON.')
        sys.exit(1)
    except yaml.YAMLError:
        print('Incorrect YAML.')
        sys.exit(1)
    except PermissionError:
        print('Permission denied.')
        sys.exit(1)
    # TODO: Надо это все отловить
