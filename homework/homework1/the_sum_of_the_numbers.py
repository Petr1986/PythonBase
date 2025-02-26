"""
Given a three-digit integer. Using // and %,
find the sum of its digits
"""

import random


def calculation_sum_num(number: int) -> int:
    min_value = 100
    max_value = 999
    if number < min_value or number > max_value:
        raise ValueError("The number must be between 100 and 999")
    return number // 100 + number % 100 // 10 + number % 10


if __name__ == "__main__":

    num = random.randint(100, 999)

    result = calculation_sum_num(num)

    print(f"Sum of the digits of a number {num}", f"equal: {result}", sep="\n")
