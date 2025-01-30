"""Assign the third digit from the end
of the positive integer to the integer variable h"""

import random


def define(num: int) -> int:
    if 100 <= num <= 10000:
        raise ValueError("out of range")
    return num % 1000 // 100


if __name__ == "__main__":

    num1 = random.randint(100, 10000)

    print(f"number = {num1}")

    third_digit = define(num1)
    print("Third digit from the end:", third_digit)
