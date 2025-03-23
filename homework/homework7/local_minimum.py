import random


def local_minimum(num: int):
    sequence = []
    for _ in range(num):
        x = random.randint(-10, 10)
        sequence.append(x)
    total = 0
    i = 0
    while i < len(sequence):
        if sequence[i] == 0:
            i += 1
            continue
        if i == 0 and sequence[i] < sequence[i + 1]:
            total += 1
        elif i == len(sequence) - 1 and sequence[i] < sequence[i - 1]:
            total += 1
        elif (
            0 < i < len(sequence) - 1
            and sequence[i] < sequence[i + 1]
            and sequence[i] < sequence[i - 1]
        ):
            total += 1
        i += 1
    return sequence, total


if __name__ == "__main__":

    number = random.randint(5, 15)

    result = local_minimum(number)

    print(
        f"For the sequence: {result[0]}", f"Sum of local minima: {result[1]}", sep="\n"
    )
