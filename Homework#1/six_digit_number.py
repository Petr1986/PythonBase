"""Given two three-digit numbers, find a six-digit number formed
from the two given numbers by adding the second number to the first"""

def concatenation(first_number: str, second_number: str) -> str:
    return first_number + second_number

if __name__ == "__main__":

    x = input('Введите первое трехзначное число: ')
    y = input('Введите второе трехзначное число: ')

    result = concatenation(x, y)

    print('Шестизначное число: ', result)