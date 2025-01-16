"""Сосчитать y = e ** a * sin(x) ** 2 - abs(x-a) / 7 двумя способами,
первый - х вводится в радианах, второй х - вводится в градусах"""

from math import e, sin, radians

if __name__ == "__main__":

#Ввод данных
    a = int(input('Введите значение а: '))
    x = int(input('Введите значение х: '))

#Вычисление уравнения, если х в радианах
    y = e ** a * sin(x) ** 2 - abs(x - a) / 7

#Вычисление уравнения, если х  в градусах
    x1 = radians(x)
    y1 = e ** a * sin(x1) ** 2 - abs(x - a) / 7

#Вывод результатов
    print('Если х задан в радианах, у =', y)
    print('Если х задан в градусах, y =', y1)