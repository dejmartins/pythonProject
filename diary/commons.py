from pathlib import Path
from utils import hash_password
import json


def get_file_path(file_name: str) -> Path:
    path = Path.cwd() / "data" / f"{file_name}.json"

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    return path


def get_file(file_name: str):
    file_path = get_file_path(file_name)

    try:
        with open(file_path, mode='r') as file:
            users = json.load(file)
            return users
    except json.decoder.JSONDecodeError:
        return []


if __name__ == "__main__":
    print(get_file_path("entries"))
