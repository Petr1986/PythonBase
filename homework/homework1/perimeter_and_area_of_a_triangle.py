"""
Given the coordinates of the three vertices of a triangle (x1,y1), (x2,y2), (x3,y3)
Find its perimeter and area
"""

import math
import random


def area_of_triangle(
    vertices_a: tuple[int, int],
    vertices_b: tuple[int, int],
    vertices_c: tuple[int, int],
) -> float:
    min_value = -20
    max_value = 20
    for x, y in (vertices_a, vertices_b, vertices_c):
        if x < min_value or x > max_value:
            raise ValueError("The x coordinates must be in the range from -20 to 20")
        if y < min_value or y > max_value:
            raise ValueError("The y coordinates must be in the range from -20 to 20")
    area = (
        abs(
            vertices_a[0] * (vertices_b[1] - vertices_c[1])
            + vertices_b[0] * (vertices_c[1] - vertices_a[1])
            + vertices_c[0] * (vertices_a[1] - vertices_b[1])
        )
        / 2
    )
    if area == 0:
        raise ValueError("The given points are collinear and do not form a triangle")
    return area


def distance(vertices1: tuple[int, int], vertices2: tuple[int, int]) -> float:
    return round(
        math.sqrt(
            (vertices2[0] - vertices1[0]) ** 2 + (vertices2[1] - vertices1[1]) ** 2
        ),
        2,
    )


def calculation_perimetr(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> float:
    return round(distance(b, c) + distance(a, c) + distance(a, b), 2)


if __name__ == "__main__":

    a1 = (random.randint(-20, 20), random.randint(-20, 20))
    b1 = (random.randint(-20, 20), random.randint(-20, 20))
    c1 = (random.randint(-20, 20), random.randint(-20, 20))

    result_perimetr = calculation_perimetr(a1, b1, c1)
    result_area = area_of_triangle(a1, b1, c1)

    print(
        f"point A = {a1}",
        f"point B = {b1}",
        f"point C = {c1}",
        distance(b1, c1),
        distance(a1, c1),
        distance(a1, b1),
        f"The perimeter of triangle ABC is: {result_perimetr:.2f}",
        f"The area of triangle ABC is: {result_area:.2f}",
        sep="\n",
    )
