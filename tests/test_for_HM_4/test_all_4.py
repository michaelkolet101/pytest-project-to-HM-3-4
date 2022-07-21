import pytest
from home_work4 import *

# val's to test with
d1 = Date(29, 2, 2016)
d2 = Date(1, 3, 2017)
d3 = Date(28, 2, 2017)
d4 = Date(31, 12, 9998)
d6 = Date(19, 4, 2016)


# test to __str__
def test__str__(capsys):
    print(d1)
    ans = capsys.readouterr()
    assert '29' in ans.out


# test to isValid valid date
def test_is_valid():
    assert d4.is_valid()


def test_to_get_next_day():
    # test to get_next_day()
    assert d3.get_next_day() == d2

def test_get_date():
    assert d2.get_date() == (1, 3, 2017)


# # test to get_next_days
def test_get_next_days():
    assert d1.get_next_days(50) == d6


# test to __lt__
def test__lt__():
    assert d3 < d4


# test to __gt__
def test__gt__():
    assert d3 > d1


def test__sub__():
    assert d6.__sub__(d1) == 50


# test for __eq__
def test__eq__():
    assert d3 == d3


# test for __ne__
def test__ne__():
    assert d3 != d4


# tes
# t for __ge__
def test__ge__():
    assert d3 >= d1


# test to __le__
def test__le__():
    assert d3 <= d4

