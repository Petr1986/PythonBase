import random


def three_integers(num1: int, num2: int, num3: int) -> bool:
    if not all(1 <= num <= 100 for num in (num1, num2, num3)):
        raise ValueError("out of range")
    return num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0


if __name__ == "__main__":

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)

    print(f"for {number1}, {number2}, {number3}")

    result = three_integers(number1, number2, number3)

    print(f"result: {result}")
