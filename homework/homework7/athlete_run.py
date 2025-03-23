import random


def athlete_run(first_run: int, finish_run: int) -> int:
    min_value_1 = 5
    max_value_1 = 10
    min_value_2 = 11
    max_value_2 = 25
    if first_run < min_value_1 or first_run > max_value_1:
        raise ValueError(
            "The first day's mileage should be between 5 and 10 kilometers."
        )
    if finish_run < min_value_2 or finish_run > max_value_2:
        raise ValueError(
            "The maximum achievable range should be between 11 and 25 kilometers."
        )
    count_day = 1
    while first_run < finish_run:
        count_day += 1
        first_run *= 1.1
    return count_day


if __name__ == "__main__":

    first_run1 = random.randint(5, 10)
    finish_run1 = random.randint(11, 25)

    result = athlete_run(first_run1, finish_run1)

    print(
        f"If on the first day the athlete was able to run kilometers {first_run1}",
        f"And it is necessary to increase the mileage to kilometers {finish_run1}",
        f"it will take {result} days",
        sep="\n",
    )
