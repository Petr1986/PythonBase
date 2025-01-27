"""Given the coordinates of the three vertices of a triangle (x1,y1), (x2,y2), (x3,y3)
Find its perimeter and area"""

import math
import random

def area_of_triangle(p1, p2, p3):
    return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2


def distance (d1: tuple[int, int],d2: tuple[int, int]) -> float:
    return math.sqrt((d2[0] - d1[0]) ** 2 + (d2[1] - d1[1]) ** 2)

def calculations(a: tuple[int, int], b: tuple[int, int], c: tuple[int,int]) -> float:
    return distance(b, c) + distance(a, c) + distance(a, b)

if __name__ == "__main__":

    while True:
        a1 = (random.randint(-100, 100), random.randint(-100, 100))
        b1 = (random.randint(-100, 100), random.randint(-100, 100))
        c1 = (random.randint(-100, 100), random.randint(-100, 100))
        if area_of_triangle(a1, b1, c1) > 0:
            break

    result_perimetr = calculations(a1, b1, c1)
    result_area = area_of_triangle(a1, b1, c1)

    print(f'Периметр треугольника АВС составляет: {result_perimetr:.2f}')
    print(f'Площадь треугольника АВС составляет: {result_area:.2f}')