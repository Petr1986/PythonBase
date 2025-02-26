import random


def factorial_of_a_number(num: int) -> int:
    if not 1 <= num <= 10:
        raise ValueError("out of range")
    total = 1
    for i in range(2, num + 1):
        total *= i
    return total


if __name__ == "__main__":

    number = random.randint(1, 10)

    result = factorial_of_a_number(number)

    print(f"Factorial of a number: {number} is {result}")
