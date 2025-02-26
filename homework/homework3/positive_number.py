import random


def positive_number(num: int) -> bool:
    if not -100 <= num <= 100:
        raise ValueError("out of range")
    return num > 0


if __name__ == "__main__":

    number = random.randint(-100, 100)

    print(f"is number {number} positive?")

    result = positive_number(number)

    print(result)
