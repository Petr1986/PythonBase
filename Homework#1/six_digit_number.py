"""Given two three-digit numbers, find a six-digit number formed
from the two given numbers by adding the second number to the first"""

import random

def concatenation(first_number: str, second_number: str) -> str:
    return first_number + second_number

if __name__ == "__main__":

    x = str(random.randint(100, 999))
    y = str(random.randint(100, 999))

    result = concatenation(x, y)

    print('Шестизначное число: ', result)