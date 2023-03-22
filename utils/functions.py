import json


def load_operations(path: str) -> dict:
    with open(path, "rb", encoding="UTF-8") as file:
        dict_ = json.load(file)
    return dict_

