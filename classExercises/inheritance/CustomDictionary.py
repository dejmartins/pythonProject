import json
from pathlib import Path


def get_path():
    path = Path.cwd() / "nigeria" / "states.json"

    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch()

    return path


def get_file():
    path = get_path()

    try:
        with open(path, mode='r') as file:
            items = json.load(file)
            return items
    except json.decoder.JSONDecodeError:
        return []


def contains(key, value):
    file = get_file()
    for elements in file:
        if key in elements:
            return True


def override(file, key, value):
    for elements in file:
        if key in elements:
            elements[key] = value


def add_file(file):
    path = get_path()
    with open(path, mode='w') as f:
        json.dump(file, f)


class CustomDictionary(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        item = {key: value}
        file = get_file()
        if not contains(key, value):
            file.append(item)
            add_file(file)


states_and_capital = CustomDictionary()
st = {"Abia": "Umuahia", "Adamawa": "Yola", "Akwa-Ibom": "Uyo"}
states_and_capital.update(st)

states_and_capital["Anambra"] = "Bauchi"
states_and_capital["Anambra"] = "Awka"
print(states_and_capital)
