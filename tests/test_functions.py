from utils import functions
from datetime import datetime


def test_datetime():
    assert functions.get_datetime("2019-01-05T00:52:30.108534") == datetime.fromisoformat("2019-01-05 00:52:30.108534")
    assert functions.get_datetime("2018-03-09T23:57:37.537412") == datetime.fromisoformat("2018-03-09 23:57:37.537412")
    assert functions.get_datetime("2018-12-22T02:02:49.564873") == datetime.fromisoformat("2018-12-22 02:02:49.564873")

