"""Calculate y = e ** a * sin(x) ** 2 - abs(x-a) / 7 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

import random
from math import e, sin, radians


def equation(a: int,x: int) -> tuple[float, float]:
    result_radians = e ** a * sin(x) ** 2 - abs(x - a) / 7
    result_degrees = e ** a * sin(radians(x)) ** 2 - abs(x - a) / 7
    return result_radians, result_degrees

if __name__ == "__main__":

    a1 = random.randint(-100, 100)
    x1 = random.randint(0, 100)

    y_radians, y_degrees = equation(a1, x1)

    print(f'If x is given in radians, у = {y_radians:.4f}')
    print(f'If x is given in degrees, y = {y_degrees:.4f}')
