from homework.homework1.perimeter_and_area_of_a_triangle import area_of_triangle, distance, calculations
import pytest


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
def test_calculations(a, b, c,  except_result):
    assert calculations(a, b, c) == except_result
