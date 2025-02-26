"""
A rectangle of size A x B is given.
How many squares with side C can be cut out of it?
A, B, C are integers. What is the area of the remaining part?
"""

import random


def result(a: int, b: int, c: int) -> tuple[float, float]:
    min_value_1 = 50
    max_value_1 = 100
    min_value_2 = 1
    max_value_2 = 49
    for x in (a, b):
        if x < min_value_1 or x > max_value_1:
            raise ValueError("Sides A and B must be in the range from 50 to 100")
    if c < min_value_2 or c > max_value_2:
        raise ValueError("Side C must be in the range from 1 to 49")
    quantity_squares = (a // c) * (b // c)
    remaining_area = a * b - quantity_squares * c**2
    return round(quantity_squares, 2), round(remaining_area, 2)


if __name__ == "__main__":

    a1 = random.randint(50, 100)
    b1 = random.randint(50, 100)
    c1 = random.randint(1, 49)

    quantity, remaining = result(a1, b1, c1)

    print(
        f"size A = {a1}",
        f"size B = {b1}",
        f"side C = {c1}",
        f"From a rectangle with sides {a1} х {b1}, can be cut out: {quantity} squares with a side {c1}",
        f"Remaining area: {remaining}",
        sep="\n",
    )
