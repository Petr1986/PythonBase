import pytest
import random
from io import StringIO

from homework.homework7.integer_powers_of_a_number import integer_powers
from homework.homework7.smallest_integer import smallest_integer
from homework.homework7.athlete_run import athlete_run
from homework.homework7.smallest_prime_divisor import smallest_prime_divisor
from homework.homework7.fibonacci_number import fibonacci_number
from homework.homework7.sequence_of_integers2 import sequence_of_integers2
from homework.homework7.the_second_largest import the_second_largest
from homework.homework7.sequence_of_integers3 import sequence_of_integers3
from homework.homework7.sequence_of_integers1 import sequence_of_integers1
from homework.homework7.reverse_number import reverse_number
from homework.homework7.local_minimum import local_minimum
from homework.homework7.guessing_game import guessing_game
from homework.homework7.enter_a_positive_number import positive_number
from homework.homework7.bisection import bisection, f
from homework.homework7.balanced_sequence import balanced_sequence


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


from unittest.mock import patch


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
def test_fibonacci_number_out_of_range(num):
    with pytest.raises(
        ValueError, match="The number must be in the range from 1 to 200"
    ):
        fibonacci_number(num)


@pytest.mark.parametrize("num", [5, 10, 15])
def test_the_second_largest(num):
    sequence, second_largest = the_second_largest(num)
    assert len(sequence) == num
    assert 0 in sequence
    if len(set(sequence)) > 1:
        sorted_sequence = sorted(set(sequence), reverse=True)
        assert second_largest == sorted_sequence[1]
    else:
        assert second_largest == 0


@pytest.mark.parametrize(
    "mock_values, expected_numbers, expected_count",
    [
        ([-8, 6, 2, -3, 9, 2, 9, 1, 5, 0, 0], [-8, 6, 2, -3, 9, 2, 9, 1, 5, 0, 0], 2),
        (
            [-5, -8, -6, 9, 5, -4, -6, 6, -5, -7, 0],
            [-5, -8, -6, 9, 5, -4, -6, 6, -5, -7, 0],
            1,
        ),
        (
            [-1, 8, -9, -4, 2, 4, 9, 4, -2, 10, 0],
            [-1, 8, -9, -4, 2, 4, 9, 4, -2, 10, 0],
            1,
        ),
    ],
)
def test_sequence_of_integers3(mock_values, expected_numbers, expected_count):
    with patch("random.randint", side_effect=mock_values):
        numbers, count = sequence_of_integers3()
        assert numbers == expected_numbers
        assert count == expected_count


@pytest.mark.parametrize(
    "mock_values, expected_numbers, expected_count",
    [
        (
            [1, 5, 7, 3, 8, -6, 9, -10, -9, 10, 0],
            [1, 5, 7, 3, 8, -6, 9, -10, -9, 10, 0],
            6,
        ),
        (
            [-5, 10, 9, -1, -2, 8, 4, -8, 0, -4, 0],
            [-5, 10, 9, -1, -2, 8, 4, -8, 0, -4, 0],
            3,
        ),
        (
            [10, 9, 6, 2, -3, -9, -5, -4, 6, 4, 0],
            [10, 9, 6, 2, -3, -9, -5, -4, 6, 4, 0],
            3,
        ),
    ],
)
def test_sequence_of_integers2(mock_values, expected_numbers, expected_count):
    with patch("random.randint", side_effect=mock_values):
        numbers, count = sequence_of_integers2()
        assert numbers == expected_numbers
        assert count == expected_count


@pytest.mark.parametrize(
    "mock_values, expected_numbers, expected_value",
    [
        (
            [-3, -5, 8, -7, -6, -8, -5, 5, 9, -7, 0],
            [-3, -5, 8, -7, -6, -8, -5, 5, 9, -7, 0],
            -1.73,
        ),
        (
            [10, -5, -2, -4, 9, 9, 9, 9, 9, -10, 0],
            [10, -5, -2, -4, 9, 9, 9, 9, 9, -10, 0],
            3.09,
        ),
        (
            [3, -8, -3, 5, 4, 2, 7, -8, -2, 8, 0],
            [3, -8, -3, 5, 4, 2, 7, -8, -2, 8, 0],
            0.73,
        ),
    ],
)
def test_sequence_of_integers1(mock_values, expected_numbers, expected_value):
    with patch("random.randint", side_effect=mock_values):
        numbers, value = sequence_of_integers1()
        assert numbers == expected_numbers
        assert value == expected_value


@pytest.mark.parametrize(
    "number, user_inputs, expected_output",
    [
        (12, ["21"], "You win"),
        (13, ["32", "32", "31"], "Try again"),
        (14, ["44", "42", "43", "41"], "Try again"),
    ],
)
def test_reverse_number(number, user_inputs, expected_output, capsys):
    def mock_input(prompt):
        return user_inputs.pop(0)

    with patch("homework.homework7.reverse_number.input", side_effect=user_inputs):
        reverse_number(number=number, user_input_func=mock_input)
        captured = capsys.readouterr()
        assert expected_output in captured.out


@pytest.mark.parametrize(
    "num, mocked_randint_values, expected_sequence, expected_total",
    [
        (5, [1, 2, 0, 3, 4], [1, 2, 0, 3, 4], 1),
        (5, [5, 1, 5, 1, 5], [5, 1, 5, 1, 5], 2),
        (3, [0, 0, 0], [0, 0, 0], 0),
        (4, [10, -10, 10, -10], [10, -10, 10, -10], 2),
    ],
)
def test_local_minimum(
    num, mocked_randint_values, expected_sequence, expected_total, monkeypatch
):
    monkeypatch.setattr(random, "randint", lambda x, y: mocked_randint_values.pop(0))
    sequence, total = local_minimum(num)
    assert sequence == expected_sequence
    assert total == expected_total


@pytest.mark.parametrize(
    "number, user_input, expected_output",
    [
        (7, ["7", "n"], "Enter your answer: You win\nLet's play again? y/n: "),
        (
            7,
            ["5", "8", "7", "n"],
            "Enter your answer: The number guessed is higher\n"
            "Enter your answer: The number guessed is less\n"
            "Enter your answer: You win\n"
            "Let's play again? y/n: ",
        ),
    ],
)
def test_guessing_game(number, user_input, expected_output):
    with patch("builtins.input", side_effect=user_input), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        guessing_game(number)
        assert mock_stdout.getvalue() == expected_output


@pytest.mark.parametrize(
    "input_values, expected",
    [
        (["1"], 1),
        (["0", "5"], 5),
        (["-1", "10"], 10),
        (["0", "0", "0"], None),
        (
            ["-1", "-1", "-1"],
            None,
        ),
    ],
)
def test_positive_number(input_values, expected, monkeypatch):
    input_generator = iter(input_values)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    if expected is not None:
        assert positive_number(input) == expected
    else:
        assert positive_number(input) is None


@pytest.mark.parametrize(
    "a, b, epsilon, expected",
    [(0, 1, 1e-6, 0.2499990463256836), (-1, 1, 1e-6, 0.0)],
)
def test_bisection(a, b, epsilon, expected):
    try:
        result = bisection(a, b, epsilon)
        assert (
            abs(result - expected) < epsilon
        ), f"Expected {expected}, but got {result}"
    except ValueError as e:
        if f(a) * f(b) >= 0:
            pytest.fail(f"Test failed because f(a) and f(b) have the same sign: {e}")
        else:
            raise e


@pytest.mark.parametrize(
    "length, expected_zeros, expected_ones, expected_twos",
    [(6, 2, 2, 2), (7, 2, 3, 2), (9, 3, 3, 3), (10, 3, 4, 3)],
)
def test_balanced_sequence(length, expected_zeros, expected_ones, expected_twos):
    sequence = balanced_sequence(length)

    assert len(sequence) == length

    count_0 = sequence.count("0")
    count_1 = sequence.count("1")
    count_2 = sequence.count("2")

    assert count_0 == expected_zeros
    assert count_1 == expected_ones
    assert count_2 == expected_twos

    assert all(c in {"0", "1", "2"} for c in sequence)


# @pytest.mark.parametrize('num', [(), (), ()])
# def test_
