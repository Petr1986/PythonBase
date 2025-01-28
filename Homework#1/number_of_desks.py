"""A school has decided to recruit three new math classes and
equip the classrooms with new desks. Two students can sit at each desk.
The number of students in each of the three classes is known.
Deduce the smallest number of desks that need to be purchased for them."""

import math
import random

def quantity_desks(students: int) -> int:
    return math.ceil(students / 2)

def total_desks(class_size: list[int]) -> int:
    return sum(quantity_desks(size) for size in class_size)

if __name__ == "__main__":

    x = [random.randint(1,40) for _ in range(3)]

    desks_needed = total_desks(x)

    print('The required number of desks is:', desks_needed)
