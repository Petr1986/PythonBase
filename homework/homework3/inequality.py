import random


def inequality(num1: int, num2: int) -> bool:
    if not all(-100 <= num <= 100 for num in (num1, num2)):
        raise ValueError("out of range")
    return num1 > 2 and num2 <= 3


if __name__ == "__main__":

    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)

    print(f"is number {number1} > 2 and {number2} <= 3?")

    result = inequality(number1, number2)

    print(result)
