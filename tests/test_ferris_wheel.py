from homework.homework1.ferris_wheel import quantity
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(8, 36, 56), (18, 34, 32), (14, 28, 28)])
def test_quantity(a,b, expected_result):
    assert quantity(a, b) == expected_result


@pytest.mark.parametrize("a, b", [(18, 10), (30, 25)])
def test_quantity_a_is_more_b(a, b):
    with pytest.raises(ValueError, match = "A should be more than B"):
        quantity(a, b)
