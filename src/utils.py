import json
from datetime import date


def create_list_all_operations(path):
    """
    Извлекаем данные из json файла
    :return: список операций
    """

    with open(path, 'r', encoding="utf-8") as file:
        operations_json = file.read()

    list_all_operations = json.loads(operations_json)

    return list_all_operations


def format_date(date_):
    """
    Форматирование даты
    :param date_: 2018-02-03T07:16:28.366141
    :return: 03.02.2018
    """

    split_date = date_.split("T")
    date_without_time = split_date[0]
    list_date = date_without_time.split("-")
    date_new = date(int(list_date[0]), int(list_date[1]), int(list_date[2]))
    date_formatted = date_new.strftime("%d.%m.%Y")

    return date_formatted


def create_necessary_operations(list_all_operations):
    """
    Создаем список последних 5 выполненных операций
    :param list_all_operations:
    :return: list_necessary_operations
    """

    list_executed_operations = []

    for operation in list_all_operations:
        if operation.get('state') == "EXECUTED":
            operation['date'] = format_date(operation['date'])
            list_executed_operations.append(operation)

    sorted_list_executed = sorted(list_executed_operations, key=lambda x: x['date'].split('.')[::-1], reverse=True)

    list_necessary_operations = sorted_list_executed[:5]

    return list_necessary_operations


def encode_card(str_card):
    """
    Замаскировываем номер счёта или карты
    :param str_card: Название и номер карты или счёта
    :return: Название и зашифрованный номер
    """

    list_card = str_card.split(" ")

    number = list_card.pop()

    code_num = ""

    if len(number) == 20:
        code_num = "**" + number[-4:]

    elif len(number) == 16:
        code_num = number[:4] + " " + number[4:6] + "** **** " + number[-4:]

    list_card.append(code_num)

    code_card = " ".join(list_card)

    return code_card


def get_formatted_operation(operation):
    """
    Форматируем операцию для выводa на экран
    :param operation:
    :return:
    """

    date_operation = operation['date']
    description = operation['description']
    transfer_to = encode_card(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    if 'from' in operation:
        transfer_from = encode_card(operation['from'])

        return (f"{date_operation} {description}\n"
                f"{transfer_from} -> {transfer_to}\n"
                f"{amount} {currency}\n")

    else:
        return ((f"{date_operation} {description}\n"
                 f"{transfer_to}\n"
                 f"{amount} {currency}\n"))
