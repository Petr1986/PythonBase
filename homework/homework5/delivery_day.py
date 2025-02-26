import random


def delivery_day(n: int, k: int) -> int:
    if not 0 <= n <= 6 or not 1 <= k <= 4:
        raise ValueError("out of range")
    if n + k > 6:
        return (n + k) - 7
    elif n + k == 5 or n + k == 6:
        return 0
    else:
        return n + k


if __name__ == "__main__":

    n1 = random.randint(0, 6)
    k1 = random.randint(1, 4)

    result = delivery_day(n1, k1)

    print(f"n = {n1} and k = {k1}, delivery day = {result}")
