import random


def palindrome_number(num1: int) -> str:
    if not 1000 <= num1 <= 9999:
        raise ValueError("out of range")
    if str(num1) == str(num1)[::-1]:
        return "Да"
    else:
        return "Нет"


if __name__ == "__main__":

    number1 = random.randint(1000, 9999)

    print(f"is {number1} palindrome?")

    result = palindrome_number(number1)

    print(result)
