from homework.homework1.the_sum_of_the_numbers import calculation
import pytest


@pytest.mark.parametrize("x, except_result", [
    (906, 15), (870, 15), (655, 16)])
def test_calculation(x, except_result):
    assert calculation(x) == except_result


@pytest.mark.parametrize("x", [55, 1001, -115])
def test_calculation_out_of_range(x):
    with pytest.raises(ValueError, match="out of range"):
        calculation(x)
