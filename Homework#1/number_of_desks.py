'''В некоторой школе решили набирать три новых математических класса и
оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.'''

import math

if __name__ == "__main__":

    #Ввод данных
    a,b,c = map(int,input('Введите через пробел количество учащихся в каждом классе (a,b,c): ').split())

    #Формула для вычисления количества парт
    def quantity_desks(x):
        return math.ceil(x / 2)

    #Количество парт по классам
    a1 = quantity_desks(a)
    b1 = quantity_desks(b)
    c1 = quantity_desks(c)

    #Общее количество парт
    desks = a1 + b1 + c1

    #Вывод результатов
    print('Необходимое количество парт равно:', desks)