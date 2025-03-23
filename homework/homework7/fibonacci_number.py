import random


def fibonacci_number(num: int):
    min_value = 1
    max_value = 200
    if num < min_value or num > max_value:
        raise ValueError("The number must be in the range from 1 to 200")
    fib1, fib2 = 0, 1
    count = 1
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
    if num == fib1 or num == fib2:
        return count
    else:
        return "Error"


if __name__ == "__main__":

    number = random.randint(1, 200)

    result = fibonacci_number(number)

    print(f"Now is {number} {result}", sep="\n")
