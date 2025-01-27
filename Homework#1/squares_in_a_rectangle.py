"""A rectangle of size A x B is given.
How many squares with side C can be cut out of it?
A, B, C are integers. What is the area of the remaining part?"""
import random


def result(a: int, b: int, c: int) -> tuple[float, float]:
    quantity_squares = (a // c) * (b // c)
    remaining_area = a * b - quantity_squares * c ** 2
    return quantity_squares, remaining_area

if __name__ == "__main__":

    while True:
        a1 = random.randint(1,100)
        b1 = random.randint(1,100)
        c1 = random.randint(1,100)
        if c1 < a1 and c1 < b1:
            break

    quantity, remaining = result(a1, b1, c1)

    print(f'Из прямоугольника со сторонами {a1} х {b1}, можно вырезать: {quantity} квадратов со стороной {c1}')
    print(f'Оставшаяся площадь: {remaining}')