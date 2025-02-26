from homework.homework3.positive_number import positive_number
from homework.homework3.odd_number import odd_number
from homework.homework3.inequality import inequality
from homework.homework3.three_integers import between_numbers
from homework.homework3.every_even import every_even
from homework.homework3.divisible_by_five import divisible_by_five
import pytest


@pytest.mark.parametrize("num, expected_result", [(-67, False), (13, True), (56, True)])
def test_positive_number(num, expected_result):
    assert positive_number(num) == expected_result


@pytest.mark.parametrize("num", [(-120), (2000), (500)])
def test_positive_number_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        positive_number(num)


@pytest.mark.parametrize("num, expected_result", [(-12, 0), (13, 1), (-25, 1)])
def test_odd_number(num, expected_result):
    assert odd_number(num) == expected_result


@pytest.mark.parametrize("num", [(-200), (5000), (-232)])
def test_odd_number_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        odd_number(num)


@pytest.mark.parametrize(
    "num1, num2, expected_result", [(94, -4, True), (11, -45, True), (-76, -76, False)]
)
def test_inequality(num1, num2, expected_result):
    assert inequality(num1, num2) == expected_result


@pytest.mark.parametrize("num1, num2", [(-150, 55), (64, 200), (-144, 320)])
def test_inequality(num1, num2):
    with pytest.raises(ValueError, match="out of range"):
        inequality(num1, num2)


@pytest.mark.parametrize(
    "num1, num2, num3, expected_result",
    [(55, 58, 14, False), (71, 70, -14, True), (-9, 39, 5, False)],
)
def test_between_numbers(num1, num2, num3, expected_result):
    assert between_numbers(num1, num2, num3) == expected_result


@pytest.mark.parametrize(
    "num1, num2, num3", [(-120, 80, 4), (-43, 254, 90), (56, -45, 3000)]
)
def test_between_numbers_out_of_range(num1, num2, num3):
    with pytest.raises(ValueError, match="out of range"):
        between_numbers(num1, num2, num3)


@pytest.mark.parametrize(
    "num1, num2, expected_result", [(-2, -70, True), (-98, 1, False), (22, -15, False)]
)
def test_every_even(num1, num2, expected_result):
    assert every_even(num1, num2) == expected_result


@pytest.mark.parametrize("num1, num2", [(-200, 54), (60, -980), (-112, 132)])
def test_every_even_out_of_range(num1, num2):
    with pytest.raises(ValueError, match="out of range"):
        every_even(num1, num2)


@pytest.mark.parametrize(
    "num1, num2, expected_result", [(8, 65, True), (87, -41, False), (-49, 3, False)]
)
def test_divisible_by_five(num1, num2, expected_result):
    assert divisible_by_five(num1, num2) == expected_result


@pytest.mark.parametrize("num1, num2", [(-150, 48), (12, 320), (564, -200)])
def test_divisible_by_five(num1, num2):
    with pytest.raises(ValueError, match="out of range"):
        divisible_by_five(num1, num2)
