"""Given two three-digit numbers, find a six-digit number formed
from the two given numbers by adding the second number to the first"""

import random


def concatenation(first_number: int, second_number: int) -> str:
    if not all(100 <= num <= 999 for num in (first_number, second_number)):
        raise ValueError("out of range")
    return str(first_number) + str(second_number)


if __name__ == "__main__":

    x = random.randint(100, 999)
    y = random.randint(100, 999)

    print(f"first number = {x}")
    print(f"second number = {y}")

    result = concatenation(x, y)

    print("Six digit number: ", result)
