import random


def sequence_of_integers2():
    count = 0
    numbers = []
    while True:
        number = random.randint(-10, 10)
        if number == 0:
            numbers.append(number)
            break
        else:
            numbers.append(number)
    for x in range(1, len(numbers) - 1):
        if numbers[x] > numbers[x - 1]:
            count += 1
    return numbers, count


if __name__ == "__main__":

    result = sequence_of_integers2()

    print(
        f"For a sequence of numbers: {result[0]}",
        f"The number of elements is greater than the previous one = {result[1]}",
        sep="\n",
    )
