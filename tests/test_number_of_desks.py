from homework.homework1.number_of_desks import quantity_desks, total_desks
import pytest

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
