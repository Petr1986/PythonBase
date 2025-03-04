import random


def sequence_of_integers1():
    total = 0
    numbers = []
    while True:
        number = random.randint(-10, 10)
        total += number
        if number == 0:
            numbers.append(number)
            break
        else:
            numbers.append(number)
    return numbers, round(total / len(numbers), 2)


if __name__ == "__main__":

    result = sequence_of_integers1()

    print(
        f"For a sequence of numbers: {result[0]}",
        f"The mean value = {result[1]}",
        sep="\n",
    )
