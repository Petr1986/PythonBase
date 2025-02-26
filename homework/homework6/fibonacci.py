import random


def fibonacci(num: int) -> int:
    if not 1 <= num <= 20:
        raise ValueError("out of range")
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, num):
            a, b = b, a + b
        return b


if __name__ == "__main__":

    number = random.randint(1, 20)

    result = fibonacci(number)

    print(f"Fibonacci number under number {number}: {result}")
