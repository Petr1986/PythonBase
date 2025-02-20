import random


def sum_of_a_series(num: int) -> int:
    if not 1 <= num <= 10:
        raise ValueError("out of range")
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total -= 1 / i
        else:
            total += 1 / i
    return round(total, 3)


if __name__ == "__main__":

    number = random.randint(1, 10)

    result = sum_of_a_series(number)

    print(f"For number: {number}, sum of a series = {result}")
