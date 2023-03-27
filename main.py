import os
import datetime
from utils.functions import load_operations, get_executed

FILE = os.path.abspath("./data/operations.json")

def main():
    operations = load_operations(FILE)
    executed = get_executed(operations)
    last_five = executed[-5:]
    for item in last_five:
        print(f"{item['date']} {item['description']}\n"
              f"{item.get('from')} -> {item['to']}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")


if __name__ == "__main__":
    main()
