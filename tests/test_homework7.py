from homework.homework7.integer_powers_of_a_number import integer_powers
from homework.homework7.smallest_integer import smallest_integer
from homework.homework7.athlete_run import athlete_run
from homework.homework7.smallest_prime_divisor import smallest_prime_divisor
from homework.homework7.fibonacci_number import fibonacci_number
import pytest


@pytest.mark.parametrize(
    "num, expected_result", [(15, [2, 4, 8]), (4, [2]), (9, [2, 4, 8])]
)
def test_integer_powers(num, expected_result):
    assert integer_powers(num) == expected_result


@pytest.mark.parametrize("num", [1, -5, 32])
def test_integer_powers_out_of_range(num):
    with pytest.raises(
        ValueError, match="The number must be in the range from -20 to 20"
    ):
        integer_powers(num)


@pytest.mark.parametrize("num, expected_result", [(19, 5), (5, 3), (6, 3)])
def test_smallest_integer(num, expected_result):
    assert smallest_integer(num) == expected_result


@pytest.mark.parametrize("num", [1, -5, 32])
def test_smallest_integer_out_of_range(num):
    with pytest.raises(
        ValueError, match="The number must be in the range from -20 to 20"
    ):
        smallest_integer(num)


@pytest.mark.parametrize(
    "first_run, finish_run, expected_result", [(7, 16, 10), (8, 23, 13), (6, 12, 9)]
)
def test_athlete_run(first_run, finish_run, expected_result):
    assert athlete_run(first_run, finish_run) == expected_result


@pytest.mark.parametrize("first_run, finish_run", [(12, 32), (-8, 4), (52, 38)])
def test_athlete_run_out_of_range(first_run, finish_run):
    with pytest.raises(
        ValueError,
        match="The first day's mileage should be between 5 and 10 kilometers.|The maximum achievable range should be between 11 and 25 kilometers.",
    ):
        athlete_run(first_run, finish_run)


@pytest.mark.parametrize("num, expected_result", [(63, 3), (92, 2), (41, 41)])
def test_smallest_prime_divisor(num, expected_result):
    assert smallest_prime_divisor(num) == expected_result


@pytest.mark.parametrize("num", [-5, 112, 155])
def test_smallest_prime_divisor_out_of_range(num):
    with pytest.raises(ValueError, match="The number must be between 2 and 100."):
        smallest_prime_divisor(num)


@pytest.mark.parametrize(
    "num, expected_result", [(52, "Error"), (55, 10), (189, "Error")]
)
def test_fibonacci_number(num, expected_result):
    assert fibonacci_number(num) == expected_result


@pytest.mark.parametrize("num", [-20, 500, 428])
def test__out_of_range(num):
    with pytest.raises(
        ValueError, match="The number must be in the range from 1 to 200"
    ):
        fibonacci_number(num)


# @pytest.mark.parametrize('num, expected_result', [(), (), ()])
# def test_


# @pytest.mark.parametrize('num', [(), (), ()])
# def test_


# @pytest.mark.parametrize('num, expected_result', [(), (), ()])
# def test_


# @pytest.mark.parametrize('num', [(), (), ()])
# def test_
