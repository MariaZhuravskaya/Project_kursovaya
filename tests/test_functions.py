from utils import functions
from datetime import datetime


def test_datetime():
    assert functions.get_datetime("2019-01-05T00:52:30.108534") == datetime.fromisoformat("2019-01-05 00:52:30.108534")
    assert functions.get_datetime("2018-03-09T23:57:37.537412") == datetime.fromisoformat("2018-03-09 23:57:37.537412")
    assert functions.get_datetime("2018-12-22T02:02:49.564873") == datetime.fromisoformat("2018-12-22 02:02:49.564873")


def test_strftime():
    assert functions.get_strftime("2019-01-05T00:52:30.108534") == '05.01.2019'
    assert functions.get_strftime("2018-03-09T23:57:37.537412") == '09.03.2018'
    assert functions.get_strftime("2018-12-22T02:02:49.564873") == '22.12.2018'


def test_from_card():
    assert functions.get_from("MasterCard 6783917276771847") == "MasterCard 6783 91** **** 1847"
    assert functions.get_from("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"
    assert functions.get_from("МИР 5211277418228469") == "МИР 5211 27** **** 8469"


def test_from_score():
    assert functions.get_from("Счет 58518872592028002662") == "Счет **2662"
    assert functions.get_from("Счет 71687416928274675290") == "Счет **5290"
    assert functions.get_from("Счет 96527012349577388612") == "Счет **8612"
