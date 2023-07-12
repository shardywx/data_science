import pytest
from main.scripts.positive_integer_set import main

@pytest.fixture
def input_list_1():
    return [1,3,6,4,1,2]

@pytest.fixture
def input_list_2():
    return [1,2,3]

@pytest.fixture
def input_list_3():
    return [-1, -3]

def test_case_1(input_list_1):
    smallest_integer = main(input_list_1)
    assert smallest_integer == 5

def test_case_2(input_list_2):
    smallest_integer = main(input_list_2)
    assert smallest_integer == 4

def test_case_3(input_list_3):
    smallest_integer = main(input_list_3)
    assert smallest_integer == 1
