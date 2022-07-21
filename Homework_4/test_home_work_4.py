from home_work4 import Date


def test_home_work():
    # val's to test with
    d1 = Date(29, 2, 2016)
    d2 = Date(1, 3, 2017)
    d3 = Date(28, 2, 2017)
    d4 = Date(31, 12, 9998)
    d6 = Date(19, 4, 2016)

    # test to __str__
    print(d1)

    # test to isValid valid date
    try:
        d4.is_valid()
        print("is_valid SUCCESS")
    except:
        print("is_valid FAIL")

    # test to get_next_day()
    if d3.get_next_day() == d2:
        print("get_next_day SUCCESS")
    else:
        print("get_next_day -> FAIL")

    # test to get_next_days
    
    if d1.get_next_days(50) == d6.get_date():
        print("get_next_days SUCCESS")
    else:
        print("get_next_days FAIL")

    # test to __it__
    if d3.__lt__((20, 2, 2018)):
        print("__it__ SUCCESS")
    else:
        print("__it__ FAIL")

    # test to __gt__
    if d3.__gt__((3, 7, 1956)):
        print("__gt__ SUCCESS")
    else:
        print("__gt__ FAIL")

    if d3.__sub__((28, 3, 2017)) == 28:
        print("__sub__ SUCCESS")
    else:
        print("__sub__ FAIL")

    # test for __eq__
    if d3.__eq__((28, 2, 2017)):
        print("__eq__ SUCCESS")
    else:
        print("__eq__ FAIL")

    # test for __ne__
    if d3.__ne__((29, 2, 2017)):
        print("__ne__ SUCCESS")
    else:
        print("__ne__ FAIL")

        # test for __ge__
    if d3.__ge__((28, 2, 2015)):
        print("__ge__ SUCCESS")
    else:
        print("__ge__ FAIL")

    # test to __le__
    if d3.__le__((31, 12, 9998)):
        print("__le__ SUCCESS")
    else:
        print("__le__ FAIL")


def main():
    test_home_work()


if __name__ == '__main__':
    main()
