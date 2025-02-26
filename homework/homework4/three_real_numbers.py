import random


def three_real_numbers(num1: float, num2: float, num3: float) -> bool:
    if not all(-5 <= num <= 10 for num in (num1, num2, num3)):
        raise ValueError("out of range")
    return all(-3 <= num <= 3 for num in (num1, num2, num3))


if __name__ == "__main__":

    number1 = random.uniform(-5, 10)
    number2 = random.uniform(-5, 10)
    number3 = random.uniform(-5, 10)

    print(f"for {number1:.2f}, {number2:.2f}, {number3:.2f}")

    result = three_real_numbers(number1, number2, number3)

    if result:
        print("УРА!")
