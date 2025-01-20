"""Calculate y = e ** a * sin(x) ** 2 - abs(x-a) / 7 in two ways,
the first - x is entered in radians, the second - x is entered in degrees"""

from math import e, sin, radians


#Функция для вычисления уравнения
def equation(a: int,x: int) -> tuple[float, float]:
    result_radians = e ** a * sin(x) ** 2 - abs(x - a) / 7
    result_degrees = e ** a * sin(radians(x)) ** 2 - abs(x - a) / 7
    return result_radians, result_degrees

if __name__ == "__main__":

#Ввод данных
    a1 = int(input('Введите значение а: '))
    x1 = int(input('Введите значение х: '))

#Вычисление уравнения
    y_radians, y_degrees = equation(a1, x1)

#Вывод результатов
    print(f'Если х задан в радианах, у = {y_radians:.4f}')
    print(f'Если х задан в градусах, y = {y_degrees:.4f}')