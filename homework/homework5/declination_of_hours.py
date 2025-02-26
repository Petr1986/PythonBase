import random


def declination_of_hours(hour: int) -> str:
    if not 1 <= hour <= 200:
        raise ValueError("out of range")
    if str(hour)[-1] == "1":
        return "Час"
    elif str(hour)[-1] in ("2", "3", "4"):
        return "Часа"
    elif str(hour)[-1] in ("0", "5", "6", "7", "8", "9"):
        return "Часов"


if __name__ == "__main__":

    hour1 = random.randint(1, 200)

    result = declination_of_hours(hour1)

    print(f"Now is {hour1} {result}")
