import random


def sequence_of_integers3():
    count = 0
    numbers = []
    while len(numbers) < 10:
        number = random.randint(-10, 10)
        numbers.append(number)
    numbers.append(0)
    for x in range(len(numbers)):
        if numbers[x] == max(numbers):
            count += 1
    return numbers, count


if __name__ == "__main__":

    result = sequence_of_integers3()

    print(
        f"For a sequence of numbers: {result[0]}",
        f"Number of elements equal to the maximum element = {result[1]}",
        sep="\n",
    )
