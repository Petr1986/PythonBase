"""
Calculate y = e ** a * sin(x) ** 2 - abs(x-a) / 7 in two ways,
the first - x is entered in radians, the second - x is entered in degrees
"""

import random
from math import e, sin, radians


def equation1(a: int, x: int) -> tuple[float, float]:
    min_value_a = -20
    max_value_a = 20
    min_value_x = 0
    max_value_x = 100
    if a < min_value_a or a > max_value_a:
        raise ValueError("The value of a must be in the range from -20 to 20")
    if x < min_value_x or x > max_value_x:
        raise ValueError("The value of x must be in the range from 0 to 100")
    result_radians = e**a * sin(x) ** 2 - abs(x - a) / 7
    result_degrees = e**a * sin(radians(x)) ** 2 - abs(x - a) / 7
    return round(result_radians, 4), round(result_degrees, 4)


if __name__ == "__main__":

    a1 = random.randint(-20, 20)
    x1 = random.randint(0, 100)

    y_radians, y_degrees = equation1(a1, x1)

    print(
        f"a = {a1}",
        f"x = {x1}",
        f"If x is given in radians, у = {y_radians:.4f}",
        f"If x is given in degrees, y = {y_degrees:.4f}",
        sep="\n",
    )
