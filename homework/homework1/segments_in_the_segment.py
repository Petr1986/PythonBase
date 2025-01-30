"""Given positive integers A and B (A > B).
On a segment of length A, the maximum possible number of segments
of length B are placed (without overlapping).
Using the division operation, find the number of segments
B placed on segment A and find the length of the unoccupied part of the segment."""

import random


def calculation(a: int, b: int) -> tuple[int, int]:
    if not 1 <= b <= 49 or not 50 <= a <= 100:
        raise ValueError("out of range")
    result_quantity = a // b
    result_remainder = a % b
    return result_quantity, result_remainder


if __name__ == "__main__":

    a1 = random.randint(50, 100)
    b1 = random.randint(1, 49)

    print(f"segment A = {a1}")
    print(f"segment B = {b1}")

    quantity, remainder = calculation(a1, b1)

    print(f"In a long segment {a1}, fits {quantity} segments of length {b1}")
    print("Remainder:", remainder)
