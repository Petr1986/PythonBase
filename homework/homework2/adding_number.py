"""Given two three-digit numbers, get a new number by adding
the second number from the right to the first without the last digits of each"""

import random


def adding_number(x: str, y: str) -> int:
    if not all(100 <= int(num) <= 999 for num in (x, y)):
        raise ValueError("out of range")
    return int(x[0 : len(x) - 1] + y[0 : len(y) - 1])


if __name__ == "__main__":

    number1 = str(random.randint(100, 999))
    number2 = str(random.randint(100, 999))

    print(f"First number = {number1}")
    print(f"Second number = {number2}")

    result = adding_number(number1, number2)

    print(f"A new number is {result}")
