from homework.homework1.celsius_to_fahrenheit import conversion
from homework.homework1.count_the_equation import equation1
from homework.homework1.count_the_equation2 import equation2
from homework.homework1.ferris_wheel import quantity
from homework.homework1.number_of_desks import quantity_desks, total_desks
from homework.homework1.perimeter_and_area_of_a_triangle import area_of_triangle, distance, calculation_perimetr
from homework.homework1.segments_in_the_segment import calculation_segments
from homework.homework1.six_digit_number import concatenation
from homework.homework1.squares_in_a_rectangle import result
from homework.homework1.the_cost_of_goods import cost
from homework.homework1.the_meaning_of_the_expression import calculation_expression
from homework.homework1.the_sum_of_the_numbers import calculation_sum_num
from homework.homework1.third_from_the_end import define
from homework.homework1.three_digit_number_problem import find_number
import pytest


@pytest.mark.parametrize(
    "x, expected_result", [(-21, -5), (4, 39), (-11, 12), (43, 109)]
)
def test_conversion(x, expected_result):
    assert conversion(x) == expected_result


@pytest.mark.parametrize("x", [-300, 1500])
def test_conversation_out_of_range(x):
    with pytest.raises(ValueError, match=f"Temperature {x} is out of range"):
        conversion(x)



@pytest.mark.parametrize(
    "a, x, expected_result",
    [
        (0, 21, (-2.3000, -2.8716)),
        (5, 38, (8.3215, 51.5401)),
        (-5, 76, (-11.5693, -11.5651)),
        (12, 76, (52150.1638, 153220.2285)),
    ],
)
def test_equation1(a, x, expected_result):
    assert equation1(a, x) == expected_result


@pytest.mark.parametrize("a, x", [(-25, 80), (-10, 115)])
def test_equation_out_of_range1(a, x):
    with pytest.raises(ValueError, match="out of range"):
        equation1(a, x)


@pytest.mark.parametrize(
    "a, b, c, d, x, expected_result",
    [
        (7, 12, -2, -12, 2, (890.1533, -15.2313)),
        (14, 4, -17, -14, 80, (1187934.6024, 1166325.7926)),
        (2, -10, -1, 20, 6, (13.4706, 12.9744)),
    ],
)
def test_equation2(a, b, c, d, x, expected_result):
    assert equation2(a, b, c, d, x) == expected_result


@pytest.mark.parametrize(
    "a, b, c, d, x", [(-22, 10, 43, -3, 150), (-14, 38, 0, -84, 64)]
)
def test_equation_out_of_range2(a, b, c, d, x):
    with pytest.raises(ValueError, match="out of range"):
        equation2(a, b, c, d, x)


@pytest.mark.parametrize(
    "a, b, expected_result", [(8, 36, 56), (18, 34, 32), (14, 28, 28)]
)
def test_quantity(a, b, expected_result):
    assert quantity(a, b) == expected_result


@pytest.mark.parametrize("a, b", [(18, 10), (30, 25)])
def test_quantity_a_is_more_b(a, b):
    with pytest.raises(ValueError, match="A should be more than B"):
        quantity(a, b)


@pytest.mark.parametrize("students, except_result", [(11, 6), (18, 9), (32, 16)])
def test_quantity_desks(students, except_result):
    assert quantity_desks(students) == except_result


@pytest.mark.parametrize("students", [-15, 43, 115])
def test_quantity_desks_out_of_range(students):
    with pytest.raises(ValueError, match = "out of range"):
        quantity_desks(students)


@pytest.mark.parametrize("students, except_result", [([3, 32, 31], 34), ([14, 17, 6], 19), ([25, 8, 24], 29)])
def test_total_desks(students, except_result):
    assert total_desks(students) == except_result


@pytest.mark.parametrize("p1, p2, p3, except_result", [
    ((-97, 41), (31, 62), (44, -19), 5320.50), ((-46, 63), (71, 78), (79, -18), 5676.00), ((-100, 34), (99, 33), (3, -46), 7908.50)])
def test_area_of_triangle(p1, p2, p3, except_result):
    assert area_of_triangle(p1, p2, p3) == except_result


@pytest.mark.parametrize("p1, p2, p3", [((20, -35), (124, -23), (115, -122)), ((-164, 152), (-34, 194), (-141, 134))])
def test_area_of_triangle_out_of_range(p1, p2, p3):
    with pytest.raises(ValueError, match = "out of range"):
        area_of_triangle(p1, p2, p3)


@pytest.mark.parametrize("d1, d2, except_result", [
    ((0, 58), (98, -11), 119.85), ((-15, 22), (98, -11), 117.72), ((-15, 22), (0, 58), 39.00)])
def test_distance(d1, d2, except_result):
    assert distance(d1, d2) == except_result


@pytest.mark.parametrize("a, b, c, except_result", [
    ((-28, 95), (22, 67), (39, -67), 367.69), ((-54, 55), (81, 16), (2, -96), 438.63), ((-72, 5), (11, 37), (40, -88), 362.86)])
def test_calculation_perimetr(a, b, c,  except_result):
    assert calculation_perimetr(a, b, c) == except_result


@pytest.mark.parametrize("a, b, except_result", [
    (54, 39, (1, 15)), (75, 17, (4, 7)), (90, 30, (3, 0))])
def test_calculation_segments(a, b, except_result):
    assert calculation_segments(a, b) == except_result


@pytest.mark.parametrize("a, b", [(-25, 80), (-10, 115)])
def test_calculation_segments_out_of_range(a, b):
    with pytest.raises(ValueError, match="out of range"):
        calculation_segments(a, b)


@pytest.mark.parametrize("first_number, second_number, except_result", [
    (324, 777, "324777"), (169, 584, "169584"), (862, 878, "862878")])
def test_concatenation(first_number, second_number, except_result):
    assert concatenation(first_number, second_number) == except_result


@pytest.mark.parametrize("first_number, second_number", [(-25, 80), (-10, 115)])
def test_concatenation_out_of_range(first_number, second_number):
    with pytest.raises(ValueError, match="out of range"):
        concatenation(first_number, second_number)


@pytest.mark.parametrize("a, b, c, except_result", [
    (81, 81, 2, (1600, 161)), (78, 54, 30, (2, 2412)), (88, 58, 14, (24, 400))])
def test_result(a, b, c, except_result):
    assert result(a, b, c) == except_result


@pytest.mark.parametrize("a, b, c", [(49, 32, 68), (-10, 115, -2), (-20, 49, 51)])
def test_result_out_of_range(a, b, c):
    with pytest.raises(ValueError, match="out of range"):
        result(a, b, c)


@pytest.mark.parametrize("k, except_result", [
    (2144, (21, 44)), (1825, (18, 25)), (3983, (39, 83))])
def test_cost(k, except_result):
    assert cost(k) == except_result


@pytest.mark.parametrize("k", [-12, 10001, 999999])
def test_cost_out_of_range(k):
    with pytest.raises(ValueError, match="out of range"):
        cost(k)


@pytest.mark.parametrize("a, b, c, d, except_result", [
    (-99, 68, -14, 43, -20195.99), (-41, 45, -88, -11, -5535.00), (83, 17, 56, 36, 4233.00)])
def test_calculation_expression(a, b, c, d, except_result):
    assert calculation_expression(a, b, c, d) == except_result


@pytest.mark.parametrize("a, b, c, d", [(-125, 100, 182, 94), (-11, 666, 151, -237), (965, -554, 98, 2)])
def test_calculation_expression_out_of_range(a, b, c, d):
    with pytest.raises(ValueError, match="out of range"):
        calculation_expression(a, b, c, d)


@pytest.mark.parametrize("x, except_result", [
    (906, 15), (870, 15), (655, 16)])
def test_calculation_sum_num(x, except_result):
    assert calculation_sum_num(x) == except_result


@pytest.mark.parametrize("x", [55, 1001, -115])
def test_calculation_sum_num_out_of_range(x):
    with pytest.raises(ValueError, match="out of range"):
        calculation_sum_num(x)


@pytest.mark.parametrize("x, except_result", [
    (8804, 8), (9531, 5), (2132, 1)])
def test_define(x, except_result):
    assert define(x) == except_result


@pytest.mark.parametrize("x", [54, 99999, -100])
def test_define_out_of_range(x):
    with pytest.raises(ValueError, match="out of range"):
        define(x)


@pytest.mark.parametrize("y, except_result", [
    (3263, 2633), (6642, 6426), (4398, 3984)])
def test_find_number(y, except_result):
    assert find_number(y) == except_result


@pytest.mark.parametrize("y", [9, -100, 10001])
def test_find_number_out_of_range(y):
    with pytest.raises(ValueError, match="out of range"):
        find_number(y)
