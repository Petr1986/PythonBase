"""Given a three-digit integer. Using // and %,
find the sum of its digits"""

import random


def calculation(x: int) -> int:
    if 100 <= x <= 999:
        raise ValueError("out of range")
    return x // 100 + x % 100 // 10 + x % 10


if __name__ == "__main__":

    num = random.randint(100, 999)

    print(f"the three-digit number = {num}")

    result = calculation(num)

    print(f"Sum of the digits of a number {num}, equal: {result}")
