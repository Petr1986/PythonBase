"""
Given positive integers A and B (A > B).
On a segment of length A, the maximum possible number of segments
of length B are placed (without overlapping).
Using the division operation, find the number of segments
B placed on segment A and find the length of the unoccupied part of the segment.
"""

import random


def calculation_segments(a: int, b: int) -> tuple[int, int]:
    min_value_a = 50
    max_value_a = 100
    min_value_b = 1
    max_value_b = 49
    if a < min_value_a or a > max_value_a:
        raise ValueError("The value of a must be in the range from 50 to 100")
    if b < min_value_b or b > max_value_b:
        raise ValueError("The value of b must be in the range from 1 to 49")
    result_quantity = a // b
    result_remainder = a % b
    return result_quantity, result_remainder


if __name__ == "__main__":

    a1 = random.randint(50, 100)
    b1 = random.randint(1, 49)

    quantity, remainder = calculation_segments(a1, b1)

    print(
        f"In a long segment {a1}, fits {quantity} segments of length {b1}",
        f"Remainder:{remainder}",
        sep="\n",
    )
