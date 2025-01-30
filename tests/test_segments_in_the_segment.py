from homework.homework1.segments_in_the_segment import calculation
import  pytest


@pytest.mark.parametrize("a, b, except_result", [
    (54, 39, (1, 15)), (75, 17, (4, 7)), (90, 30, (3, 0))])
def test_calculation(a, b, except_result):
    assert calculation(a, b) == except_result


@pytest.mark.parametrize("a, b", [(-25, 80), (-10, 115)])
def test_calculation_out_of_range(a, b):
    with pytest.raises(ValueError, match="out of range"):
        calculation(a, b)
