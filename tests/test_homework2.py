import pytest
from homework.homework2.rearranged_numbers import swap


@pytest.mark.parametrize(
    "x, expected_result", [('877', 778), ('878', 878), ('811', 118)]
)
def test_swap(x, expected_result):
    assert swap(x) == expected_result


@pytest.mark.parametrize("x", ['50', '-100', '1000'])
def test_swap_out_of_range(x):
    with pytest.raises(ValueError, match = "out of range"):
        swap(x)
