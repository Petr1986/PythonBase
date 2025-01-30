from homework.homework1.squares_in_a_rectangle import result
import pytest


@pytest.mark.parametrize("a, b, c, except_result", [
    (81, 81, 2, (1600, 161)), (78, 54, 30, (2, 2412)), (88, 58, 14, (24, 400))])
def test_result(a, b, c, except_result):
    assert result(a, b, c) == except_result


@pytest.mark.parametrize("a, b, c", [(49, 32, 68), (-10, 115, -2), (-20, 49, 51)])
def test_result_out_of_range(a, b, c):
    with pytest.raises(ValueError, match="out of range"):
        result(a, b, c)
