import os
from utils.functions import load_operations, get_executed, sort_list, date_format

FILE = os.path.abspath("./data/operations.json")


def main():
    operations = load_operations(FILE)
    executed = get_executed(operations)
    sorted_operations = sort_list(executed)
    last_five = sorted_operations[:5]
    for item in last_five:
        date = date_format(item.get('date'))
        description = item.get('description')
        from_ = item.get('from')
        to_ = item.get('to')
        amount = item.get('operationAmount').get('amount')
        currency = item.get('operationAmount').get('currency').get('name')
        print(f"{date} {description}\n"
              f"{from_} -> {to_}\n"
              f"{amount} {currency}\n")


if __name__ == "__main__":
    main()
