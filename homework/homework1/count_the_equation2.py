"""Calculate y = e ** a * sin(x) ** 2 - sqrt(abs(c-b ** 2) / a) + d a<>0 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

import random
from math import e, sin, radians, sqrt


def equation2(a: int, b: int, c: int, d: int, x: int) -> tuple[float, float]:
    if not all(-20 <= v <= 20 for v in (a, b, c, d)) or not (0 <= x <= 100):
        raise ValueError("out of range")
    result_radians = e**a * sin(x) ** 2 - sqrt(abs((c - b**2) / a)) + d
    result_degrees = e**a * sin(radians(x)) ** 2 - sqrt(abs((c - b**2) / a)) + d
    return round(result_radians, 4), round(result_degrees, 4)


if __name__ == "__main__":

    a1 = random.randint(-20, -1) if random.random() < 0.5 else random.randint(1, 20)
    b1 = random.randint(-20, 20)
    c1 = random.randint(-20, 20)
    d1 = random.randint(-20, 20)
    x1 = random.randint(0, 100)
    print(f"a = {a1}")
    print(f"b = {b1}")
    print(f"c = {c1}")
    print(f"d = {d1}")
    print(f"x = {x1}")

    y_radians, y_degrees = equation2(a1, b1, c1, d1, x1)

    print(f"If x is given in radians, y = {y_radians:.4f}")
    print(f"If x is given in degrees, y = {y_degrees:.4f}")
