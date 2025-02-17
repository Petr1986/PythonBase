import random


def time_of_year(month: int) -> str:
    if not 1 <= month <= 12:
        raise ValueError("out of range")
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"


if __name__ == "__main__":

    month1 = random.randint(1, 12)

    print(f"If month {month1}")

    result = time_of_year(month1)

    print(f"Now {result}")
