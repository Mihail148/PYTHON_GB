import json
import os

#{level: {id: name}}


def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    with open(file_name, 'w') as f:
        json.dump({}, f)
    return {}


def enter_users(level: str, id: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id in value:
            raise ValueError("id уже существует")

    data.setdefault(level, {})
    data[level].setdefault(id, name)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return


if __name__ == '__main__':
    enter_users('5', '12345656', 'Alex', 'data1.json')