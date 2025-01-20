"""A rectangle of size A x B is given.
How many squares with side C can be cut out of it?
A, B, C are integers. What is the area of the remaining part?"""

#Функция для вычисления результатов
def result(a: int, b: int, c: int) -> tuple[float, float]:
    quantity_squares = (a // c) * (b // c)
    remaining_area = a * b - quantity_squares * c ** 2
    return quantity_squares, remaining_area

if __name__ == "__main__":

#Ввод данных
    a1, b1 = map(int, input('Введи длинны А и В, через пробел: ').split())
    c1 = int(input('Введите длину С: '))

#Вычисление результатов
    quantity, remaining = result(a1, b1, c1)

#Вывод результатов
    print(f'Из прямоугольника со сторонами {a1} х {b1}, можно вырезать: {quantity} квадратов со стороной {c1}')
    print(f'Оставшаяся площадь: {remaining}')