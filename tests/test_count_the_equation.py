from homework.homework1.count_the_equation import equation
import pytest


@pytest.mark.parametrize(
    "a, x, expected_result",
    [
        (0, 21, (-2.3000, -2.8716)),
        (5, 38, (8.3215, 51.5401)),
        (-5, 76, (-11.5693, -11.5651)),
        (12, 76, (52150.1638, 153220.2285)),
    ],
)
def test_equation(a, x, expected_result):
    assert equation(a, x) == expected_result


@pytest.mark.parametrize("a, x", [(-25, 80), (-10, 115)])
def test_equation_out_of_range(a, x):
    with pytest.raises(ValueError, match="out of range"):
        equation(a, x)
