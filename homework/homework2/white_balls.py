"""There are N white and M black balls in a basket,
two balls are drawn at random, what is the probability that they are both white?
Determine the probability as a percentage, with two decimal places"""

import random


def probability_balls(white_balls: int, black_balls: int) -> float:
    if not all(4 <= i <= 10 for i in (white_balls, black_balls)):
        raise ValueError("out of range")
    total_balls = white_balls + black_balls
    numbers_white = (white_balls * (white_balls - 1)) / 2
    numbers_all = (total_balls * (total_balls - 1)) / 2
    return round((numbers_white / numbers_all) * 100, 2)


if __name__ == "__main__":

    wb = random.randint(4, 10)
    bb = random.randint(4, 10)

    print(f"number of white balls = {wb}")
    print(f"number of black balls = {bb}")

    result = probability_balls(wb, bb)

    print(f"probability that they are both white = {result} %")
