"""A school has decided to recruit three new math classes and
equip the classrooms with new desks. Two students can sit at each desk.
The number of students in each of the three classes is known.
Deduce the smallest number of desks that need to be purchased for them."""

import math

def quantity_desks(students: int) -> int:
    return math.ceil(students / 2)

def total_desks(class_size: list[int]) -> int:
    return sum(quantity_desks(size) for size in class_size)

if __name__ == "__main__":

    x = list(map(int,input('Введите через пробел количество учащихся в каждом классе (a,b,c): ').split()))

    desks_needed = total_desks(x)

    print('Необходимое количество парт равно:', desks_needed)