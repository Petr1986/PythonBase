from homework.homework4.even_three_digit_number import even_three_digit_number
from homework.homework4.three_integers import three_integers
from homework.homework4.three_real_numbers import three_real_numbers
from homework.homework4.name_check import name_check
from homework.homework4.modulus_of_a_number import modulus_of_a_number
from homework.homework4.cell_color import cell_color
from homework.homework4.quarter_plane import quarter_plane
from homework.homework4.palindrome_number import palindrome_number
import pytest


@pytest.mark.parametrize("num1, expected_result", [(980, 1), (483, 0), (598, 1)])
def test_even_three_digit_number(num1, expected_result):
    assert even_three_digit_number(num1) == expected_result


@pytest.mark.parametrize("num1", [(-112), (1002), (2400)])
def test_even_three_digit_number_out_of_range(num1):
    with pytest.raises(ValueError, match="out of range"):
        even_three_digit_number(num1)


@pytest.mark.parametrize(
    "num1, num2, num3, expected_result",
    [(90, 21, 96, True), (77, 25, 35, False), (42, 34, 22, True)],
)
def test_three_integers(num1, num2, num3, expected_result):
    assert three_integers(num1, num2, num3) == expected_result


@pytest.mark.parametrize(
    "num1, num2, num3", [(-12, 50, 64), (10, 112, 58), (42, 89, -545)]
)
def test_three_integers_out_of_range(num1, num2, num3):
    with pytest.raises(ValueError, match="out of range"):
        three_integers(num1, num2, num3)


@pytest.mark.parametrize(
    "num1, num2, num3, expected_result",
    [(-1.17, 1.68, 2.91, True), (7.93, 0.31, 2.04, False), (3.29, 3.39, 0.76, False)],
)
def test_three_real_numbers(num1, num2, num3, expected_result):
    assert three_real_numbers(num1, num2, num3) == expected_result


@pytest.mark.parametrize(
    "num1, num2, num3", [(-7.3, 2.8, 9.4), (3.2, 11.5, -4.8), (-1.3, 6.1, -12.6)]
)
def test_three_real_numbers_out_of_range(num1, num2, num3):
    with pytest.raises(ValueError, match="out of range"):
        three_real_numbers(num1, num2, num3)


@pytest.mark.parametrize(
    "name, expected_result",
    [
        ("Kirill", "Добро пожаловать, Kirill"),
        ("Petr", "Добро пожаловать, Petr"),
        ("", "Пожалуйста авторизуйтесь"),
    ],
)
def test_name_check(name, expected_result):
    assert name_check(name) == expected_result


def test_name_check_type_error():
    with pytest.raises(TypeError, match="name must be string"):
        name_check(2)


@pytest.mark.parametrize("num1, expected_result", [(-9, 9), (5, 5), (-8, 8)])
def test_modulus_of_a_number(num1, expected_result):
    assert modulus_of_a_number(num1) == expected_result


@pytest.mark.parametrize("num1", [(-12), (55), (200)])
def test_modulus_of_a_number(num1):
    with pytest.raises(ValueError, match="out of range"):
        modulus_of_a_number(num1)


@pytest.mark.parametrize(
    "x, y, expected_result", [(6, 2, "black"), (1, 2, "white"), (1, 1, "black")]
)
def test_cell_color(x, y, expected_result):
    assert cell_color(x, y) == expected_result


@pytest.mark.parametrize("x, y", [(9, 2), (6, -3), (17, -24)])
def test_cell_color_out_of_range(x, y):
    with pytest.raises(ValueError, match="out of range"):
        cell_color(x, y)


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (16, -13, "fourth quarter"),
        (-6, -11, "third quarter"),
        (-3, 13, "second quarter"),
    ],
)
def test_quarter_plane(x, y, expected_result):
    assert quarter_plane(x, y) == expected_result


@pytest.mark.parametrize("x, y", [(-65, 15), (4, 85), (63, -54)])
def test_quarter_plane_out_of_range(x, y):
    with pytest.raises(ValueError, match="out of range"):
        quarter_plane(x, y)


@pytest.mark.parametrize(
    "num, expected_result", [(1661, "Да"), (1656, "Нет"), (6814, "Нет")]
)
def test_palindrome_number(num, expected_result):
    assert palindrome_number(num) == expected_result


@pytest.mark.parametrize("num", [(352), (10001), (-22)])
def test_palindrome_number_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        palindrome_number(num)
