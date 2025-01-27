"""Calculate y = e ** a * sin(x) ** 2 - sqrt(abs(c-b ** 2) / a) + d a<>0 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

import random
from math import e, sin, radians, sqrt

def equation(a: int, b: int, c: int, d: int, x: int) -> tuple[float, float]:
    result_radians = e ** a * sin(x) ** 2 - sqrt(abs(c - b ** 2) / a) + d
    result_degrees = e ** a * sin(radians(x)) ** 2 - sqrt(abs((c - b ** 2) / a)) + d
    return result_radians, result_degrees

if __name__ == "__main__":

    a1 = random.randint(-100, 100)
    b1 = random.randint(-100, 100)
    c1 = random.randint(-100, 100)
    d1 = random.randint(-100, 100)
    x1 = random.randint(0, 100)

    y_radians, y_degrees = equation(a1, b1, c1, d1, x1)

    print(f'Если x задан в радианах, y = {y_radians}')
    print(f'Если x задан в градусах, y = {y_degrees}')