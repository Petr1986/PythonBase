from homework.homework6.sum_of_a_series import sum_of_a_series
from homework.homework6.factorial_of_a_number import factorial_of_a_number
from homework.homework6.even_number import even_number
from homework.homework6.prime_numbers_in_the_range import prime_numbers_in_the_range
from homework.homework6.sum_of_cubes import sum_of_cubes
from homework.homework6.right_triangles import right_triangles
from homework.homework6.count_coin_combination import count_coin_combination
from homework.homework6.fibonacci import fibonacci
from homework.homework6.sum_of_a_series2 import sum_of_a_series2
from homework.homework6.perfect_number import perfect_number, is_perfect_number
import pytest
from unittest.mock import patch


@pytest.mark.parametrize("num1, expected_result", [(9, 0.746), (3, 0.833), (7, 0.76)])
def test_sum_of_a_series(num1, expected_result):
    assert sum_of_a_series(num1) == expected_result


@pytest.mark.parametrize("num1", [-5, 11, 52])
def test_sum_of_a_series_out_of_range(num1):
    with pytest.raises(ValueError, match="out of range"):
        sum_of_a_series(num1)


@pytest.mark.parametrize("num1, expected_result", [(5, 120), (10, 3628800), (7, 5040)])
def test_factorial_of_a_number(num1, expected_result):
    assert factorial_of_a_number(num1)


@pytest.mark.parametrize("num1", [-20, 54, 222])
def test_factorial_of_a_number_out_of_range(num1):
    with pytest.raises(ValueError, match="out of range"):
        factorial_of_a_number(num1)


@pytest.mark.parametrize(
    "num1, mock_values, expected_result",
    [
        (3, [2, 5, 7], "There are even ones"),
        (4, [1, 3, 5, 7], "There are no even ones"),
        (2, [8, 10], "There are even ones"),
    ],
)
def test_even_number(num1, mock_values, expected_result):
    with patch("random.randint", side_effect=mock_values):
        result = even_number(num1)
        assert isinstance(result, tuple)
        assert isinstance(result[0], list)
        assert result[0] == mock_values
        assert result[1] == expected_result


@pytest.mark.parametrize("num1", [0, -3, 12])
def test_even_number_out_of_range(num1):
    with pytest.raises(ValueError, match="out of range"):
        even_number(num1)


@pytest.mark.parametrize(
    "num1, num2, expected_result",
    [
        (10, 46, [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]),
        (8, 39, [11, 13, 17, 19, 23, 29, 31, 37]),
        (26, 48, [29, 31, 37, 41, 43, 47]),
    ],
)
def test_prime_numbers_in_the_range(num1, num2, expected_result):
    assert prime_numbers_in_the_range(num1, num2) == expected_result


@pytest.mark.parametrize("num1, num2", [(1, -20), (-5, 33), (12, 54)])
def test_prime_numbers_in_the_range_out_of_range(num1, num2):
    with pytest.raises(ValueError, match="out of range"):
        prime_numbers_in_the_range(num1, num2)


def test_sum_of_cubes():
    expected_result = [153, 370, 371, 407]
    assert sum_of_cubes() == expected_result


@pytest.mark.parametrize("num1, expected_result", [(105, 55), (59, 25), (136, 76)])
def test_right_triangles(num1, expected_result):
    assert right_triangles(num1) == expected_result


@pytest.mark.parametrize("num1", [10, -15, 547])
def test_right_triangles_out_of_range(num1):
    with pytest.raises(ValueError, match="out of range"):
        right_triangles(num1)


@pytest.mark.parametrize(
    "a1, a2, a3, a4, s, expected_result",
    [
        (1, 5, 3, 10, 84, [(0, 2, 0, 8), (0, 2, 2, 7), (1, 4, 1, 7), (1, 4, 3, 6)]),
        (
            4,
            4,
            6,
            7,
            20,
            [
                (0, 0, 0, 2),
                (0, 0, 2, 1),
                (0, 0, 4, 0),
                (1, 2, 1, 1),
                (1, 2, 3, 0),
                (2, 4, 0, 1),
                (2, 4, 2, 0),
                (3, 1, 1, 1),
                (3, 1, 3, 0),
                (4, 3, 0, 1),
                (4, 3, 2, 0),
            ],
        ),
        (
            5,
            4,
            3,
            7,
            26,
            [
                (0, 3, 0, 2),
                (0, 3, 2, 1),
                (1, 0, 1, 2),
                (1, 0, 3, 1),
                (2, 2, 0, 2),
                (2, 2, 2, 1),
                (3, 4, 1, 1),
                (3, 4, 3, 0),
                (4, 1, 0, 2),
                (4, 1, 2, 1),
                (5, 3, 1, 1),
                (5, 3, 3, 0),
            ],
        ),
    ],
)
def test_count_coin_combination(a1, a2, a3, a4, s, expected_result):
    assert count_coin_combination(a1, a2, a3, a4, s) == expected_result


@pytest.mark.parametrize(
    "a1, a2, a3, a4, s",
    [(-2, 8, 12, 54, 98), (2, 4, 9, 6, 235), (-5, -32, -18, -58, -224)],
)
def test_count_coin_combination_out_of_range(a1, a2, a3, a4, s):
    with pytest.raises(ValueError, match="out of range"):
        count_coin_combination(a1, a2, a3, a4, s)


@pytest.mark.parametrize("num, expected_result", [(4, 2), (12, 89), (5, 3)])
def test_fibonacci(num, expected_result):
    assert fibonacci(num)


@pytest.mark.parametrize("num", [-5, 50, -54])
def test_fibonacci_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        fibonacci(num)


@pytest.mark.parametrize(
    "num, expected_result", [(4, 7106), (7, 125230946), (6, 4149986)]
)
def test_sum_of_a_series2(num, expected_result):
    assert sum_of_a_series2(num) == expected_result


@pytest.mark.parametrize("num", [-2, 50, 343])
def test_sum_of_a_series2_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        sum_of_a_series2(num)


@pytest.mark.parametrize(
    "num, expected_result", [(52, [6, 28]), (818, [6, 28, 496]), (8, [6])]
)
def test_perfect_number(num, expected_result):
    assert perfect_number(num)


@pytest.mark.parametrize("num", [-220, 123456, -2500])
def test_perfect_number_out_of_range(num):
    with pytest.raises(ValueError, match="out of range"):
        perfect_number(num)


@pytest.mark.parametrize("num, expected_result", [(16, False), (6, True), (54, False)])
def test_is_perfect_number(num, expected_result):
    assert is_perfect_number(num) == expected_result
