import random


def every_even(num1: int, num2: int) -> bool:
    if not all(-100 <= num <= 100 for num in (num1, num2)):
        raise ValueError("out of range")
    return num1 % 2 == 0 and num2 % 2 == 0


if __name__ == "__main__":

    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)

    print(f"is number {number1} and {number2} even?")

    result = every_even(number1, number2)

    print(result)
