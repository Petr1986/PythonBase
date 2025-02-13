import random


def modulus_of_a_number(num1: int) -> int:
    if not -10 <= num1 <= 10:
        raise ValueError("out of range")
    if num1 < 0:
        num1 = -num1
    return num1


if __name__ == "__main__":

    number1 = random.randint(-10, 10)

    result = modulus_of_a_number(number1)

    print(f"modulus of number {number1} is {result}")
