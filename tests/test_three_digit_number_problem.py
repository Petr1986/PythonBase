from homework.homework1.three_digit_number_problem import find_number
import pytest


@pytest.mark.parametrize("y, except_result", [
    (3263, 2633), (6642, 6426), (4398, 3984)])
def test_find_number(y, except_result):
    assert find_number(y) == except_result


@pytest.mark.parametrize("y", [9, -100, 10001])
def test_find_number_out_of_range(y):
    with pytest.raises(ValueError, match="out of range"):
        find_number(y)
