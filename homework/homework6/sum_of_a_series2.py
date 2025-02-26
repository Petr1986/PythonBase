import random


def sum_of_a_series2(num: int) -> int:
    if not 1 <= num <= 10:
        raise ValueError("out of range")
    total_sum = 0
    for i in range(1, num + 1):
        total = 1
        for j in range(i, 2 * i + 1):
            total *= j
        total_sum += total
    return total_sum


if __name__ == "__main__":

    number = random.randint(1, 10)

    result = sum_of_a_series2(number)

    print(f"For {number} sum of a series: {result}")
