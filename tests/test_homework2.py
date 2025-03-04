from homework.homework2.rearranged_numbers import swap
from homework.homework2.adding_number import adding_number
from homework.homework2.extracting_the_root_of_a_power import extracting_root
from homework.homework2.finish_time import find_time
from homework.homework2.empty_bottles import needed_bags
from homework.homework2.white_balls import probability_balls
from homework.homework2.number_of_seconds import find_second
from homework.homework2.degrees_minute_second import dms_to_radian
import pytest


@pytest.mark.parametrize(
    "x, expected_result", [("877", 778), ("878", 878), ("811", 118)]
)
def test_swap(x, expected_result):
    assert swap(x) == expected_result


@pytest.mark.parametrize("x", ["50", "-100", "1000"])
def test_swap_out_of_range(x):
    with pytest.raises(ValueError, match="out of range"):
        swap(x)


@pytest.mark.parametrize(
    "x, y, expected_result",
    [("288", "492", 2849), ("480", "443", 4844), ("764", "891", 7689)],
)
def test_adding_number(x, y, expected_result):
    assert adding_number(x, y) == expected_result


@pytest.mark.parametrize("x, y", [("-545", "1000"), ("32", "200"), ("321", "-12")])
def test_adding_number_out_of_range(x, y):
    with pytest.raises(
        ValueError, match="Numbers must be three digits in the range from 100 to 999"
    ):
        adding_number(x, y)


@pytest.mark.parametrize(
    "num, k, m, expected_result",
    [(1, 3, 4, 3.246), (3, 3, 7, 128.877), (4, 2, 10, 20.047)],
)
def test_extracting_root(num, k, m, expected_result):
    assert extracting_root(num, k, m) == expected_result


@pytest.mark.parametrize("num, k, m", [(6, -10, 12), (0, 8, 6), (4, 3, 3)])
def test_extracting_root_out_of_range(num, k, m):
    with pytest.raises(ValueError, match="out of range"):
        extracting_root(num, k, m)


@pytest.mark.parametrize(
    "first_time, second_time, expected_result",
    [
        ((2, 6, 39), (2, 50, 46), 2647),
        ((2, 7, 11), (2, 52, 59), 2748),
        ((2, 20, 25), (2, 53, 37), 1992),
    ],
)
def test_find_time(first_time, second_time, expected_result):
    assert find_time(first_time, second_time) == expected_result


@pytest.mark.parametrize(
    "first_time, second_time",
    [
        ((3, 12, 64), (0, 8, 32)),
        ((23, 56, 8), (8, 94, 30)),
        ((18, 24, 30), (89, 34, 12)),
    ],
)
def test_find_time_out_of_range(first_time, second_time):
    with pytest.raises(ValueError, match="out of range"):
        find_time(first_time, second_time)


@pytest.mark.parametrize("k, n, expected_result", [(5, 41, 9), (5, 60, 12), (6, 45, 8)])
def test_needed_bags(k, n, expected_result):
    assert needed_bags(n, k) == expected_result


@pytest.mark.parametrize("n, k", [(10, 6), (30, 10), (100, 12)])
def test_needed_bags_out_of_range(n, k):
    with pytest.raises(ValueError, match="out of range"):
        needed_bags(n, k)


@pytest.mark.parametrize(
    "wb, bb, expected_result", [(6, 7, 19.23), (10, 6, 37.5), (9, 8, 26.47)]
)
def test_probability_balls(wb, bb, expected_result):
    assert probability_balls(wb, bb) == expected_result


@pytest.mark.parametrize("wb, bb", [(3, 8), (6, 12), (1, 15)])
def test_probability_balls_out_of_range(wb, bb):
    with pytest.raises(ValueError, match="out of range"):
        probability_balls(wb, bb)


@pytest.mark.parametrize(
    "sec, expected_result",
    [(9308, (155, 2, 8, 35)), (4250, (70, 1, 50, 10)), (6589, (109, 1, 49, 49))],
)
def test_find_second(sec, expected_result):
    assert find_second(sec) == expected_result


@pytest.mark.parametrize("sec", [3600, 20, 15000])
def test_find_second_out_of_range(sec):
    with pytest.raises(ValueError, match="out of range"):
        find_second(sec)


@pytest.mark.parametrize(
    "degrees, minutes, seconds, expected_result",
    [
        (127, 49, 30, (2.23, 0.79, 0.61, -1.29)),
        (170, 3, 39, (2.97, 0.17, -0.98, -0.18)),
        (119, 39, 59, (2.09, 0.87, -0.49, -1.76)),
    ],
)
def test_dms_to_radian(degrees, minutes, seconds, expected_result):
    assert dms_to_radian(degrees, minutes, seconds) == expected_result


@pytest.mark.parametrize(
    "degrees, minutes, seconds", [(-20, 15, 36), (110, 67, 42), (30, 54, -10)]
)
def test_dms_to_radian(degrees, minutes, seconds):
    with pytest.raises(
        ValueError,
        match="Minutes and seconds must be between 1 and 59|Degrees can range from 0 to 360",
    ):
        dms_to_radian(degrees, minutes, seconds)
