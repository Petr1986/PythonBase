import random


def even_three_digit_number(num1: int) -> bool:
    if not -100 <= num1 <= 999:
        raise ValueError("out of range")
    return len(str(num1)) == 3 and num1 > 0 and num1 % 2 == 0


if __name__ == "__main__":

    number1 = random.randint(-100, 999)

    print(f"for {number1}")

    result = int(even_three_digit_number(number1))

    print(f"result: {result}")
