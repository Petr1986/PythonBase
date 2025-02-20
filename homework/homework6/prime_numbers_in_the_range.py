import random


def prime_numbers_in_the_range(num1: int, num2: int) -> list:
    if not all(3 <= num <= 50 for num in (num1, num2)):
        raise ValueError("out of range")
    lst = []
    for i in range(num1, num2 + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            lst.append(i)
    return lst


if __name__ == "__main__":

    number1 = random.randint(3, 50)
    number2 = random.randint(number1, 50)

    result = prime_numbers_in_the_range(number1, number2)

    print(f"for range {number1} {number2}. List of Prime Numbers: {result}")
