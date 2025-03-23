import random


def smallest_prime_divisor(num: int) -> int:
    min_value = 2
    max_value = 100
    if num < min_value or num > max_value:
        raise ValueError("The number must be between 2 and 100.")
    if num % 2 == 0:
        return 2
    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            return divisor
        divisor += 2
    return num


if __name__ == "__main__":

    number = random.randint(2, 100)

    result = smallest_prime_divisor(number)

    print(f"For number: {number}", f"Smallest prime divisor: {result}", sep="\n")
