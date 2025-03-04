import random


def the_second_largest(number: int) -> tuple[list, int]:
    sequence = []
    while len(sequence) < number - 1:
        num = random.randint(0, 30)
        sequence.append(num)
    sequence.append(0)
    second_largest = 0
    for x in sequence:
        if second_largest < x < max(sequence):
            second_largest = x
    return sequence, second_largest


if __name__ == "__main__":

    number1 = random.randint(2, 20)

    result = the_second_largest(number1)

    print(f"In sequence: {result[0]}", f"the second largest: {result[1]}", sep="\n")
