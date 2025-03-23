"""Calculate y = e ** a * sin(x) ** 2 - abs(x-a) / 7 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

import random
from math import e, sin, radians


def equation1(a: int, x: int) -> tuple[float, float]:
    if not -20 <= a <= 20 or not 0 <= x <= 100:
        raise ValueError("out of range")
    result_radians = e**a * sin(x) ** 2 - abs(x - a) / 7
    result_degrees = e**a * sin(radians(x)) ** 2 - abs(x - a) / 7
    return round(result_radians, 4), round(result_degrees, 4)


if __name__ == "__main__":

    a1 = random.randint(-20, 20)
    x1 = random.randint(0, 100)

    print(f"a = {a1}")
    print(f"x = {x1}")

    y_radians, y_degrees = equation1(a1, x1)

    print(f"If x is given in radians, у = {y_radians:.4f}")
    print(f"If x is given in degrees, y = {y_degrees:.4f}")
