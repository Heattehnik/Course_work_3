import os
import datetime
from utils.functions import load_operations, get_executed


def main():
    path = os.path.abspath("./data/operations.json")
    operations = load_operations(path)
    executed = get_executed(operations)
    last_five = executed[-5:]
    for item in last_five:
        print(f"{item['date']} {item['description']}\n"
              f"{item['from']} -> {item['to']}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")

if __name__ == "__main__":
    main()