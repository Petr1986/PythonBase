import random


def is_perfect_number(num1: int) -> bool:
    divisors = 1
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0:
            divisors += i
            if i != num1 // i:
                divisors += num1 // i
    return num1 == divisors


def perfect_number(num: int) -> list:
    if not 3 <= num <= 5000:
        raise ValueError("out of range")
    perfect_numbers = []
    for i in range(2, num):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


if __name__ == "__main__":

    number = random.randint(3, 5000)

    result = perfect_number(number)

    print(f"Now is {number} {result}")
