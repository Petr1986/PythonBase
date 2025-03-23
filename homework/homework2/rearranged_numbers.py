"""Given a three-digit integer, get a new number with the first and last digits swapped"""

import random


def swap(number: str) -> int:
    if not 100 <= int(number) <= 999:
        raise ValueError("out of range")
    return int(number[-1] + number[1 : len(number) - 1] + number[0])


if __name__ == "__main__":

    number1 = str(random.randint(100, 999))

    result = swap(number1)

    print(f"Original number {number1} modified number {result}")
