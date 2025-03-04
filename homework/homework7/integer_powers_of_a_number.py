import random


def integer_powers(num: int):
    min_value = 3
    max_value = 20
    if num < min_value or num > max_value:
        raise ValueError("The number must be in the range from -20 to 20")
    total = 1
    numbers = []
    while total < num:
        total *= 2
        if total < num:
            numbers.append(total)
    return numbers


if __name__ == "__main__":

    number = random.randint(3, 20)

    result = integer_powers(number)

    print(f"For {number}", result, sep="\n")
