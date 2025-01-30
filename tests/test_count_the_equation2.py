from homework.homework1.count_the_equation2 import equation
import pytest


@pytest.mark.parametrize("a, b, c, d, x, expected_result", [
    (7, 12, -2, -12, 2, (890.1533, -15.2313)), (14, 4, -17, -14, 80, (1187934.6024, 1166325.7926)), (2, -10, -1, 20, 6, (13.4706, 12.9744))
])
def test_equation2(a, b, c, d, x, expected_result):
    assert equation(a, b, c, d, x) == expected_result


@pytest.mark.parametrize("a, b, c, d, x", [(-22, 10, 43, -3, 150), (-14, 38, 0, -84, 64)])
def test_equation_out_of_range2(a, b, c, d, x):
    with pytest.raises(ValueError, match = "out of range"):
        equation(a, b, c, d, x)
