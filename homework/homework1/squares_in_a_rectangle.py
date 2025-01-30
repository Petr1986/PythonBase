"""A rectangle of size A x B is given.
How many squares with side C can be cut out of it?
A, B, C are integers. What is the area of the remaining part?"""

import random


def result(a: int, b: int, c: int) -> tuple[float, float]:
    if not all(50 <= num <= 100 for num in (a, b)) or 1 <= c <= 49:
        raise ValueError("out of range")
    quantity_squares = (a // c) * (b // c)
    remaining_area = a * b - quantity_squares * c**2
    return quantity_squares, remaining_area


if __name__ == "__main__":

    a1 = random.randint(50, 100)
    b1 = random.randint(50, 100)
    c1 = random.randint(1, 49)

    print(f"size A = {a1}")
    print(f"size B = {b1}")
    print(f"side C = {c1}")

    quantity, remaining = result(a1, b1, c1)

    print(
        f"From a rectangle with sides {a1} х {b1}, can be cut out: {quantity} squares with a side {c1}"
    )
    print(f"Remaining area: {remaining}")
