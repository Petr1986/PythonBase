from homework.homework1.six_digit_number import concatenation
import  pytest


@pytest.mark.parametrize("first_number, second_number, except_result", [
    (324, 777, "324777"), (169, 584, "169584"), (862, 878, "862878")])
def test_concatenation(first_number, second_number, except_result):
    assert concatenation(first_number, second_number) == except_result


@pytest.mark.parametrize("first_number, second_number", [(-25, 80), (-10, 115)])
def test_concatenation_out_of_range(first_number, second_number):
    with pytest.raises(ValueError, match="out of range"):
        concatenation(first_number, second_number)
