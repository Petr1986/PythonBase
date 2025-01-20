"""Calculate y = e ** a * sin(x) ** 2 - sqrt(abs(c-b ** 2) / a) + d a<>0 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

from math import e, sin, radians, sqrt

#Функция для вычисления уравнения
def equation(a: int, b: int, c: int, d: int, x: int) -> tuple[float, float]:
    result_radians = e ** a * sin(x) ** 2 - sqrt(abs(c - b ** 2) / a) + d
    result_degrees = e ** a * sin(radians(x)) ** 2 - sqrt(abs((c - b ** 2) / a)) + d
    return result_radians, result_degrees

if __name__ == "__main__":

#Ввод данных
    a1 = int(input('Введите значение a: '))
    b1 = int(input('Введите значение b: '))
    c1 = int(input('Введите значение c: '))
    d1 = int(input('Введите значение d: '))
    x1 = int(input('Введите значение x: '))

#Вычисление уравнения
    y_radians, y_degrees = equation(a1, b1, c1, d1, x1)

#Вывод результатов
    print(f'Если x задан в радианах, y = {y_radians}')
    print(f'Если x задан в градусах, y = {y_degrees}')