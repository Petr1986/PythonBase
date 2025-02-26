"""
Assign the third digit from the end
of the positive integer to the integer variable h
"""

import random


def define(number: int) -> int:
    min_value = 100
    max_value = 10000
    if number < min_value or number > max_value:
        raise ValueError("The number must be between 100 and 10000")
    return number % 1000 // 100


if __name__ == "__main__":

    num1 = random.randint(100, 10000)

    third_digit = define(num1)
    print(f"number = {num1}", f"Third digit from the end: {third_digit}", sep="\n")
