"""Given the coordinates of the three vertices of a triangle (x1,y1), (x2,y2), (x3,y3)
Find its perimeter and area"""

import math

#Функция для вычисления длинны стороны треугольника
def distance (d1: tuple[int, int],d2: tuple[int, int]) -> float:
    return math.sqrt((d2[0] - d1[0]) ** 2 + (d2[1] - d1[1]) ** 2)

#Функция для вычисления периметра
def calculations(a: tuple[int, int], b: tuple[int, int], c: tuple[int,int]) -> tuple[float, float]:
    #Длины сторон
    side_a = distance(b, c)
    side_b = distance(a, c)
    side_c = distance(a, b)

    #Периметр
    perimetr = side_a + side_b + side_c

    #Полупериметр
    s = perimetr / 2

    #Площадь по формуле Герона
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

    return perimetr, area

if __name__ == "__main__":

# Ввод исходных данных
    a1 = tuple(map(int, input('Введите (через пробел) координаты (x1,y1) вершины А:').split()))
    b1 = tuple(map(int, input('Введите (через пробел) координаты (x2,y2) вершины В:').split()))
    c1 = tuple(map(int, input('Введите (через пробел) координаты (x3,y3) вершины С:').split()))

# Вычисление периметра и площади по формуле Герона
    result_perimetr, result_area = calculations(a1, b1, c1)

# Вывод результатов
    print(f'Периметр треугольника АВС составляет: {result_perimetr:.2f}')
    print(f'Площадь треугольника АВС составляет: {result_area:.2f}')