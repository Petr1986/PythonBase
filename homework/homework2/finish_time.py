"""The finish time of the winner and
the next competitor is known (hours, minutes, seconds).
Find the time lag in seconds"""

import random


def find_time(first_time: tuple[int, int, int], second_time: tuple[int, int, int]) -> int:
    if not all(0 <= i <= 59 for i in (first_time[2], second_time[2])) or not 1 <= first_time[0] <= 2 or not 0 <= first_time[1] <= 30 or not 31 <= second_time[1] <= 59:
        raise ValueError("out of range")
    finish1 = first_time[0] * 3600 + first_time[1] * 60 + first_time[2]
    finish2 = second_time[0] * 3600 + second_time[1] * 60 + second_time[2]
    return finish2 - finish1


if __name__ == "__main__":

    time1 = (random.randint(1, 2), random.randint(0, 30), random.randint(0, 59))
    time2 = (2, random.randint(31, 59), random.randint(0, 59))

    print(f'First time = {time1}')
    print(f'Second time = {time2}')

    result = find_time(time1, time2)

    print(f'Time lag = {result} seconds')
