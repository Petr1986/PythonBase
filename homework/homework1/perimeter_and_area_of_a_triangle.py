"""Given the coordinates of the three vertices of a triangle (x1,y1), (x2,y2), (x3,y3)
Find its perimeter and area"""

import math
import random


def area_of_triangle(
    p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]
) -> float:
    if not all(-100 <= coord <= -1 for coord in (p1[0], p3[1])) or not all(
        0 <= coord <= 100 for coord in (p1[1], p2[0], p2[1], p3[0])
    ):
        raise ValueError("out of range")
    return (
        abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
        / 2
    )


def distance(d1: tuple[int, int], d2: tuple[int, int]) -> float:
    return round(math.sqrt((d2[0] - d1[0]) ** 2 + (d2[1] - d1[1]) ** 2), 2)


def calculation_perimetr(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> float:
    return round(distance(b, c) + distance(a, c) + distance(a, b), 2)


if __name__ == "__main__":

    a1 = (random.randint(-100, -1), random.randint(0, 100))
    b1 = (random.randint(0, 100), random.randint(0, 100))
    c1 = (random.randint(0, 100), random.randint(-100, -1))

    print(f"point A = {a1}")
    print(f"point B = {b1}")
    print(f"point C = {c1}")

    print(distance(b1, c1))
    print(distance(a1, c1))
    print(distance(a1, b1))

    result_perimetr = calculation_perimetr(a1, b1, c1)
    result_area = area_of_triangle(a1, b1, c1)

    print(f"The perimeter of triangle ABC is: {result_perimetr:.2f}")
    print(f"The area of triangle ABC is: {result_area:.2f}")
