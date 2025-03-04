import random


def smallest_integer(num: int):
    min_value = 3
    max_value = 20
    if num < min_value or num > max_value:
        raise ValueError("The number must be in the range from -20 to 20")
    total = 1
    count = 0
    while total < num:
        total *= 2
        count += 1
    return count


if __name__ == "__main__":

    number = random.randint(3, 20)

    result = smallest_integer(number)

    print(f"For {number}", result, sep="\n")
