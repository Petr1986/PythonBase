import random


def odd_number(num: int) -> bool:
    if not -100 <= num <= 100:
        raise ValueError("out of range")
    return num % 2 != 0


if __name__ == "__main__":

    number = random.randint(-100, 100)

    print(f"is number {number} odd?")

    result = int(odd_number(number))

    print(result)
