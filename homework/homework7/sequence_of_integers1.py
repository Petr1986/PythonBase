import random


def sequence_of_integers1():
    total = 0
    numbers = []
    while len(numbers) < 10:
        number = random.randint(-10, 10)
        total += number
        numbers.append(number)
    numbers.append(0)
    return numbers, round(total / len(numbers), 2)


if __name__ == "__main__":

    result = sequence_of_integers1()

    print(
        f"For a sequence of numbers: {result[0]}",
        f"The mean value = {result[1]}",
        sep="\n",
    )
