import math

# Функция для вычисления расстояния между двумя точками
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Ввод координат вершин треугольника
print("Введите координаты вершин треугольника:")
x1, y1 = map(float, input("Вершина A (x1 y1): ").split())
x2, y2 = map(float, input("Вершина B (x2 y2): ").split())
x3, y3 = map(float, input("Вершина C (x3 y3): ").split())

# Координаты
A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

# Длины сторон
a = distance(B, C)
b = distance(A, C)
c = distance(A, B)

# Периметр
perimeter = a + b + c

# Полупериметр
s = perimeter / 2

# Площадь по формуле Герона
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Результаты
print(f"\nСтороны треугольника: a = {a:.2f}, b = {b:.2f}, c = {c:.2f}")
print(f"Периметр: {perimeter:.2f}")
print(f"Площадь: {area:.2f}")
