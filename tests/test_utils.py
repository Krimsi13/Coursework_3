from src.utils import create_list_all_operations, format_date, encode_card, get_formatted_operation
from config import ROOT_DIR
import os.path

DATA_DIR = os.path.join(ROOT_DIR, "tests", "test.json")


def test_create_list_all_operations():
    assert create_list_all_operations(DATA_DIR) == [1, 2, 3]


def test_format_date():
    assert format_date('2018-02-03T07:16:28.366141') == '03.02.2018'


def test_encode_card():
    assert encode_card('Cчет 64686473678894779589') == 'Cчет **9589'
    assert encode_card('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


operation = {'id': 863064926,
             'state': 'EXECUTED',
             'date': '08.12.2019',
             'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада',
             'to': 'Счет 90424923579946435907'}

second_operation = {'id': 114832369,
                    'state': 'EXECUTED',
                    'date': '07.12.2019',
                    'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                    'description': 'Перевод организации',
                    'from': 'Visa Classic 2842878893689012',
                    'to': 'Счет 35158586384610753655'}


def test_get_formatted_operation():
    assert get_formatted_operation(operation) == "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD\n"
    assert get_formatted_operation(second_operation) == ("07.12.2019 Перевод организации\n"
                                                         "Visa Classic 2842 87** **** 9012"
                                                         " -> Счет **3655\n48150.39 USD\n")
