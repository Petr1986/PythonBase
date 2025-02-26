from pickle import FALSE

from homework.homework5.cabinet_size import cabinet_size
from homework.homework5.time_of_year import time_of_year
from homework.homework5.time_to_walk import time_to_walk
from homework.homework5.chocolate import chocolate
from homework.homework5.meaning_u import meaning_u
from homework.homework5.decision_making import decision_making
from homework.homework5.delivery_day import delivery_day
from homework.homework5.intersecting_events import intersecting_events
from homework.homework5.find_intersection import find_intersection
from homework.homework5.right_cost import ruble_cost, kopeck_cost
from homework.homework5.radar_direction import radar_direction
from homework.homework5.day_of_year import day_of_year
import pytest


@pytest.mark.parametrize(
    "h, w, h1, w1, expected_result",
    [(16, 22, 78, 46, True), (29, 80, 8, 22, False), (55, 92, 36, 62, False)],
)
def test_cabinet_size(h, w, h1, w1, expected_result):
    assert cabinet_size(h, w, h1, w1) == expected_result


@pytest.mark.parametrize(
    "h, w, h1, w1", [(3, 8, 22, 115), (22, 200, -50, 20), (222, 118, -32, 562)]
)
def test_cabinet_size_out_of_range(h, w, h1, w1):
    with pytest.raises(ValueError, match="out of range"):
        cabinet_size(h, w, h1, w1)


@pytest.mark.parametrize(
    "month, expected_result", [(10, "Autumn"), (5, "Spring"), (8, "Summer")]
)
def test_time_of_year(month, expected_result):
    assert time_of_year(month) == expected_result


@pytest.mark.parametrize("month", [(-112), (54), (22)])
def test_time_of_year_out_of_range(month):
    with pytest.raises(ValueError, match="out of range"):
        time_of_year(month)


@pytest.mark.parametrize(
    "temperature_b, temperature, weather, expected_result",
    [
        (36.1, 22, "sunny", "go walk"),
        (36.4, 20, "cloudy", "The weather is bad"),
        (36.3, 30, "worm", "Extremal temperature"),
    ],
)
def test_time_to_walk(temperature_b, temperature, weather, expected_result):
    assert time_to_walk(temperature_b, temperature, weather) == expected_result


@pytest.mark.parametrize(
    "temperature_b, temperature, weather",
    [(-32, 18, "sunny"), (36.6, -52, "cloudy"), (32.3, 58, "snow")],
)
def test_time_to_walk_out_of_range(temperature_b, temperature, weather):
    with pytest.raises(ValueError, match="out of range"):
        time_to_walk(temperature_b, temperature, weather)


@pytest.mark.parametrize(
    "slices, k_slices, expected_result",
    [(20, 10, True), (19, 6, False), (20, 8, False)],
)
def test_chocolate(slices, k_slices, expected_result):
    assert chocolate(slices, k_slices) == expected_result


@pytest.mark.parametrize("slices, k_slices", [(5, 8), (15, -3), (12, 32)])
def test_chocolate_out_of_range(slices, k_slices):
    with pytest.raises(ValueError, match="out of range"):
        chocolate(slices, k_slices)


@pytest.mark.parametrize(
    "x, y, z, expected_result",
    [
        (15.83, 2.26, 0.45, 0.92),
        (2, 2, 4, "You can't divide by zero"),
        (11.76, -16.32, -2.33, 2.04),
    ],
)
def test_meaning_u(x, y, z, expected_result):
    assert meaning_u(x, y, z) == expected_result


@pytest.mark.parametrize("x, y, z", [(-25, 12.2, 84), (14, 56, 3.42), (21, -55.5, 40)])
def test_meaning_u_out_of_range(x, y, z):
    with pytest.raises(ValueError, match="out of range"):
        meaning_u(x, y, z)


@pytest.mark.parametrize(
    "money, drinker, gave, misser, expected_result",
    [
        (True, True, False, False, "he is a drinker"),
        (False, False, False, True, "you have no money"),
        (True, False, True, False, "you can land"),
    ],
)
def test_decision_making(money, drinker, gave, misser, expected_result):
    assert decision_making(money, drinker, gave, misser) == expected_result


@pytest.mark.parametrize(
    "money, drinker, gave, misser",
    [
        (1, 2, 3, 4),
        (
            "you can land",
            "you are misser",
            "he doesn't pay his debts",
            "he is a drinker",
        ),
        (True, 12, False, "he is a drinker"),
    ],
)
def test_decision_making_must_be_bool(money, drinker, gave, misser):
    with pytest.raises(TypeError, match="must be bool"):
        decision_making(money, drinker, gave, misser)


@pytest.mark.parametrize("n, k, expected_result", [(1, 4, 0), (2, 1, 3), (6, 2, 1)])
def test_delivery_day(n, k, expected_result):
    assert delivery_day(n, k) == expected_result


@pytest.mark.parametrize("n, k", [(2, 8), (9, 1), (-3, 18)])
def test_delivery_day_out_of_range(n, k):
    with pytest.raises(ValueError, match="out of range"):
        delivery_day(n, k)


@pytest.mark.parametrize(
    "h_start1, m_start1, s_start1,"
    "h_finish1, m_finish1, s_finish1,"
    "h_start2, m_start2, s_start2,"
    "h_finish2, m_finish2, s_finish2, expected_result",
    [
        (10, 45, 13, 13, 56, 52, 8, 11, 5, 9, 6, 33, "events do not intersect"),
        (10, 0, 26, 12, 17, 49, 8, 34, 12, 16, 31, 40, "intersecting events"),
        (8, 9, 53, 9, 18, 6, 8, 59, 30, 16, 13, 46, "intersecting events"),
    ],
)
def test_intersecting_events(
    h_start1,
    m_start1,
    s_start1,
    h_finish1,
    m_finish1,
    s_finish1,
    h_start2,
    m_start2,
    s_start2,
    h_finish2,
    m_finish2,
    s_finish2,
    expected_result,
):
    assert (
        intersecting_events(
            h_start1,
            m_start1,
            s_start1,
            h_finish1,
            m_finish1,
            s_finish1,
            h_start2,
            m_start2,
            s_start2,
            h_finish2,
            m_finish2,
            s_finish2,
        )
        == expected_result
    )


@pytest.mark.parametrize(
    "h_start1, m_start1, s_start1,"
    "h_finish1, m_finish1, s_finish1,"
    "h_start2, m_start2, s_start2,"
    "h_finish2, m_finish2, s_finish2",
    [
        (8, 18, 234, 43, 12, 45, 78, 34, 78, -12, 54, 98),
        (43, -54, 12, 45, 65, 98, 75, 43, -9, 3, 56, 65),
        (-56, 43, 65, 12, 34, 56, 78, 90, 12, -10, -34, -45),
    ],
)
def test_intersecting_events(
    h_start1,
    m_start1,
    s_start1,
    h_finish1,
    m_finish1,
    s_finish1,
    h_start2,
    m_start2,
    s_start2,
    h_finish2,
    m_finish2,
    s_finish2,
):
    with pytest.raises(ValueError, match="out of range"):
        intersecting_events(
            h_start1,
            m_start1,
            s_start1,
            h_finish1,
            m_finish1,
            s_finish1,
            h_start2,
            m_start2,
            s_start2,
            h_finish2,
            m_finish2,
            s_finish2,
        )


@pytest.mark.parametrize(
    "x1, y1, w1, h1," "x2, y2, w2, h2, expected_result",
    [
        (49, 36, 17, 9, 44, 22, 3, 5, "the rectangles do not intersect"),
        (22, 20, 14, 8, 23, 16, 20, 7, (23, 20, 36, 23)),
        (25, 8, 20, 18, 27, 27, 9, 7, "the rectangles do not intersect"),
    ],
)
def test_find_intersection(x1, y1, w1, h1, x2, y2, w2, h2, expected_result):
    assert find_intersection(x1, y1, w1, h1, x2, y2, w2, h2) == expected_result


@pytest.mark.parametrize(
    "x1, y1, w1, h1," "x2, y2, w2, h2",
    [
        (-20, 23, 65, 98, 54, 76, -98, 6),
        (-43, 56, -10, 28, 93, 81, -73, -6),
        (20, -38, 46, 44, 66, 77, 88, 99),
    ],
)
def test_find_intersection_out_of_range(x1, y1, w1, h1, x2, y2, w2, h2):
    with pytest.raises(ValueError, match="out of range"):
        find_intersection(x1, y1, w1, h1, x2, y2, w2, h2)


@pytest.mark.parametrize(
    "ruble, expected_result", [(53.02, "рубля"), (89.54, "рублей"), (81.29, "рубль")]
)
def test_ruble_cost(ruble, expected_result):
    assert ruble_cost(ruble) == expected_result


@pytest.mark.parametrize("ruble", [(-22.0), (965), (-321)])
def test_ruble_cost_out_of_range(ruble):
    with pytest.raises(ValueError, match="out of range"):
        ruble_cost(ruble)


@pytest.mark.parametrize(
    "ruble, expected_result",
    [(53.02, "копейки"), (81.29, "копеек"), (97.91, "копейка")],
)
def test_kopeck_cost(ruble, expected_result):
    assert kopeck_cost(ruble) == expected_result


@pytest.mark.parametrize("ruble", [(-332), (2000), (-53)])
def test_kopeck_cost_out_of_range(ruble):
    with pytest.raises(ValueError, match="out of range"):
        kopeck_cost(ruble)


@pytest.mark.parametrize(
    "current, command1, command2, expected_result",
    [("east", -1, 2, "north"), ("south", 2, 2, "south"), ("east", 1, -1, "east")],
)
def test_radar_direction(current, command1, command2, expected_result):
    assert radar_direction(current, command1, command2) == expected_result


@pytest.mark.parametrize(
    "current, command1, command2", [("east", 0, 0), ("east", -5, 2), ("east", 12, 54)]
)
def test_radar_direction_out_of_range(current, command1, command2):
    with pytest.raises(ValueError, match="out of range"):
        radar_direction(current, command1, command2)


@pytest.mark.parametrize(
    "day_k, day_n, expected_result",
    [(124, 6, "Wednesday"), (47, 4, "Monday"), (289, 6, "Sunday")],
)
def test_day_of_year(day_k, day_n, expected_result):
    assert day_of_year(day_k, day_n) == expected_result


@pytest.mark.parametrize("day_k, day_n", [(-20, 54), (154, 8), (22, 348)])
def test_day_of_year_out_of_range(day_k, day_n):
    with pytest.raises(ValueError, match="out of range"):
        day_of_year(day_k, day_n)
