import pytest
from home_work_3 import *

data_set = {
    3322117: {
        "name": "Tal",
        "gender": "male",
        "height": 1.90,
        "age": 22
    },
    176864301: {
        "gender": "female",
        "age": 57,
        "height": 1.65,
        "name": "Anat"
    },
    176756301: {
        "gender": "female",
        "age": 80,
        "height": 1.30,
        "name": "branch"
    },
    176654301: {
        "gender": "female",
        "age": 30,
        "height": 1.65,
        "name": "hna"
    },
    176867301: {
        "gender": "male",
        "age": 37,
        "height": 1.80,
        "name": "fafu"
    },
    176826401: {
        "gender": "female",
        "age": 19,
        "height": 1.65,
        "name": "roza"
    },
    176864551: {
        "gender": "male",
        "age": 25,
        "height": 1.85,
        "name": "victor"
    },
    165864651: {
        "gender": "female",
        "age": 41,
        "height": 1.68,
        "name": "banana"
    },
    176436301: {
        "gender": "male",
        "age": 15,
        "height": 1.65,
        "name": "banani"
    }
}


@pytest.fixture
def test_averageIMP():
    assert averageIMP([1, 2, 3, 4, 5]) == 3


@pytest.fixture
def test_medianIMP():
    assert medianIMP([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5


def test_find_median_average(test_averageIMP, test_medianIMP):
    lst = find_median_average(data_set)
    assert (lst[0] == 36.22222222222222 and lst[1] == 30)


def test_ChaeckValIMP(capsys):
    ChaeckValIMP(data_set)
    ans = capsys.readouterr()
    assert ans.err == ""


def test_split_male_female():

    lst_of_dict = split_male_female(data_set)
    assert 'female' not in lst_of_dict[0]
    assert 'male' not in lst_of_dict[1]


def test_print_values_above(capsys):
    print_values_above(data_set, 30)
    ans = capsys.readouterr()
    assert '22' not in ans.out
