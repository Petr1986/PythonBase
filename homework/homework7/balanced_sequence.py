import random


def balanced_sequence(length: int) -> str:
    zeros = twos = length // 3
    ones = length - (zeros + twos)
    sequence = ""
    count_0 = count_1 = count_2 = 0
    while len(sequence) < length:
        num = random.choice("012")
        if num == "0" and count_0 < zeros:
            sequence += num
            count_0 += 1
        elif num == "1" and count_1 < ones:
            sequence += num
            count_1 += 1
        elif num == "2" and count_2 < twos:
            sequence += num
            count_2 += 1
    return sequence


if __name__ == "__main__":

    length1 = random.randint(5, 20)

    print(balanced_sequence(length1))
