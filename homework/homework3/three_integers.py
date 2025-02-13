import random


def between_numbers(num1: int, num2: int, num3: int) -> bool:
    if not all(-100 <= num <= 100 for num in (num1, num2, num3)):
        raise ValueError("out of range")
    return num1 <= num2 <= num3 or num3 <= num2 <= num1


if __name__ == "__main__":

    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    number3 = random.randint(-100, 100)

    print(f"is number {number2} between {number1} and {number3}")

    result = int(between_numbers(number1, number2, number3))

    print(result)
