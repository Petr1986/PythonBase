import random


def day_of_year(day_k: int, day_n: int) -> str:
    if not 1 <= day_k <= 365 or not 1 <= day_n <= 7:
        raise ValueError("out of range")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_of_week = (day_n + (day_k - 1)) % 7
    return day[day_of_week]


if __name__ == "__main__":

    day_k1 = random.randint(1, 365)
    day_n1 = random.randint(1, 7)

    result = day_of_year(day_k1, day_n1)

    print(f"If K = {day_k1}, and N = {day_n1}")
    print(result)
