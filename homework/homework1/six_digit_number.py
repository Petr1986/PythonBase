"""
Given two three-digit numbers, find a six-digit number formed
from the two given numbers by adding the second number to the first
"""

import random


def concatenation(first_number: int, second_number: int) -> str:
    min_value = 100
    max_value = 999
    if first_number < min_value or second_number < min_value:
        raise ValueError("The number must be greater than 99")
    if first_number > max_value or second_number > max_value:
        raise ValueError("The number must be less than 1000")
    return str(first_number) + str(second_number)


if __name__ == "__main__":

    x = random.randint(100, 999)
    y = random.randint(100, 999)

    result = concatenation(x, y)

    print(
        f"first number = {x}",
        f"second number = {y}",
        f"Six digit number: {result}",
        sep="\n",
    )
