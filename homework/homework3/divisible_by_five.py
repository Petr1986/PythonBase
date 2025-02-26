import random


def divisible_by_five(num1: int, num2: int) -> bool:
    if not all(-100 <= num <= 100 for num in (num1, num2)):
        raise ValueError("out of range")
    return num1 % 5 == 0 or num2 % 5 == 0


if __name__ == "__main__":

    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)

    print(f"is number {number1} or {number2} divisible by five?")

    result = divisible_by_five(number1, number2)

    print(result)
