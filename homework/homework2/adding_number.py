"""Given two three-digit numbers, get a new number by adding
the second number from the right to the first without the last digits of each"""

import random


def adding_number(number_1: str, number_2: str) -> int:
    min_value = 100
    max_value = 999
    for x in (number_1, number_2):
        if int(x) < min_value or int(x) > max_value:
            raise ValueError(
                "Numbers must be three digits in the range from 100 to 999"
            )
    return int(number_1[0 : len(number_1) - 1] + number_2[0 : len(number_2) - 1])


if __name__ == "__main__":

    number1 = str(random.randint(100, 999))
    number2 = str(random.randint(100, 999))

    result = adding_number(number1, number2)

    print(
        f"First number = {number1}",
        f"Second number = {number2}",
        f"A new number is {result}",
        sep="\n",
    )
