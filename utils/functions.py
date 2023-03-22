import json


def load_operations(path: str) -> list:
    with open(path, "rb", encoding="UTF-8") as file:
        list_ = json.load(file)
    return list_


def get_executed(operations: list) -> list:
    result_list = []
    for item in operations:
        if item["state"] == "EXECUTED":
            result_list.append(item)
    return result_list

