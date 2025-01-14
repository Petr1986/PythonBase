'''Дан прямоугольник размером А х В.
Сколько квадратов со стороной С можно вырезать из него?
А, В, С - целые числа. Какова площадь оставшейся части'''

if __name__ == "__main__":

    #Ввод данных
    A, B = map(int, input('Введи длинны А и В, через пробел: ').split())
    C = int(input('Введите длину С: '))

    #Функция для вычисления количества квадратов
    def squares (a,b,c):
        return (a // c) * (b // c)

    quantity_squares = squares(A,B,C)

    area_squares = quantity_squares * C ** 2

    area_rectangle = A * B

    remaining_area = area_rectangle - area_squares

    #Вывод результатов
    print(f'Из прямоугольника со сторонами А х В, можно вырезать: {quantity_squares} квадратов со стороной {C}')
    print(f'Оставшаяся площадь: {remaining_area}')