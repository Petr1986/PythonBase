"""
Calculate y = e ** a * sin(x) ** 2 - sqrt(abs(c-b ** 2) / a) + d a<>0 in two ways,
the first - x is entered in radians, the second - x is entered in degrees
"""

import random
from math import e, sin, radians, sqrt


def equation2(a: int, b: int, c: int, d: int, x: int) -> tuple[float, float]:
    min_value_1 = -20
    max_value_1 = 20
    min_value_2 = 0
    max_value_2 = 100
    for num in (a, b, c, d):
        if num < min_value_1 or num > max_value_1:
            raise ValueError("The value must be in the range from -20 to 20")
    if x < min_value_2 or x > max_value_2:
        raise ValueError("The value must be in the range from 0 to 100")
    result_radians = e**a * sin(x) ** 2 - sqrt(abs((c - b**2) / a)) + d
    result_degrees = e**a * sin(radians(x)) ** 2 - sqrt(abs((c - b**2) / a)) + d
    return round(result_radians, 4), round(result_degrees, 4)


if __name__ == "__main__":

    a1 = random.randint(-20, -1) if random.random() < 0.5 else random.randint(1, 20)
    b1 = random.randint(-20, 20)
    c1 = random.randint(-20, 20)
    d1 = random.randint(-20, 20)
    x1 = random.randint(0, 100)

    y_radians, y_degrees = equation2(a1, b1, c1, d1, x1)

    print(
        f"a = {a1}",
        f"b = {b1}",
        f"c = {c1}",
        f"d = {d1}",
        f"x = {x1}",
        f"If x is given in radians, y = {y_radians:.4f}",
        f"If x is given in degrees, y = {y_degrees:.4f}",
        sep="\n",
    )
