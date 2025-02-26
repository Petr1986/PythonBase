import random
import math


def right_triangles(num: int) -> int:
    count = 0
    if not 50 <= num <= 200:
        raise ValueError("out of range")
    for a in range(1, num):
        for b in range(a, num):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and c < num:
                count += 1
    return count


if __name__ == "__main__":

    number = random.randint(50, 200)

    result = right_triangles(number)

    print(f"For {number}, right triangles: {result}")
