import json
import datetime


def load_operations(path: str) -> list:
    """Функция принимает в качестве аргумента строку с путем файла json
    и возвращает список словарей
    """
    with open(path, "r", encoding="UTF-8") as file:
        list_ = json.load(file)
    return list_


def sort_list(operations: list) -> list:
    """
    Функция принимает список словарей и сортирует его по дате.
    И возвращает отсортированный список.
    :param operations:
    :return:
    """
    operations.sort(key=lambda x: x.get('date'), reverse=True)
    return operations


def get_executed(operations: list) -> list:
    result_list = []
    for item in operations:
        if item.get('state') == 'EXECUTED':
            result_list.append(item)
    return result_list


def date_format(date: str) -> str:
    """
    Функция принимает строку с датой в формате 2019-08-26T10:50:58.294041
    и возвращет в формате 26.08.2019
    :param date:
    :return:
    """
    input_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    formated_date = input_date.strftime('%d.%m.%Y')

    return formated_date


def mask_card(card: str) -> str:
    """
    Функция принимает строку и скрывает элементы по маске
    :param card:
    :return: скрытая строка
    """
    if not card:
        return ''
    card_data = card.split(' ')
    if card_data[0] == 'Счет':
        return card_data[0] + ' **' + card_data[1][-4:]
    card_number = card_data[-1][:4] + ' ' + card_data[-1][4:6] + '** **** ' + card_data[-1][-4:]
    return ' '.join(card_data[:-1]) + ' ' + card_number

