import json


def load_operations(path: str) -> list:
    with open(path, "r", encoding="UTF-8") as file:
        list_ = json.load(file)
    return list_


def get_executed(operations: list) -> list:
    result_list = []
    for item in operations:
        if item.get('state') == 'EXECUTED':
            result_list.append(item)
    print(result_list)
    return result_list

