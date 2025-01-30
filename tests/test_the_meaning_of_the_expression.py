from homework.homework1.the_meaning_of_the_expression import calculation
import pytest


@pytest.mark.parametrize("a, b, c, d, except_result", [
    (-99, 68, -14, 43, -20195.99), (-41, 45, -88, -11, -5535.00), (83, 17, 56, 36, 4233.00)])
def test_calculation(a, b, c, d, except_result):
    assert calculation(a, b, c, d) == except_result


@pytest.mark.parametrize("a, b, c, d", [(-125, 100, 182, 94), (-11, 666, 151, -237), (965, -554, 98, 2)])
def test_calculation_out_of_range(a, b, c, d):
    with pytest.raises(ValueError, match="out of range"):
        calculation(a, b, c, d)
