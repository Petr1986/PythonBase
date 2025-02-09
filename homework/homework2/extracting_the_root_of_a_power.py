"""A three-digit number N is given.
Raise this number to the 10th power, write k times in a row.
Extract the root of the degree M from the resulting number.
Output the answer with three decimal places."""

import random


def extracting_root(num: int, k: int, m: int) -> float:
    if not all( 1 <= i <= 5 for i in(num, k)) or not 4 <= m <= 10:
        raise ValueError('out of range')
    a = str(num ** 10) * k
    return round(int(a) ** (1/m), 3)


if __name__ == "__main__":

    num1 = random.randint(1, 5)
    k1 = random.randint(1, 5)
    m1 = random.randint(4, 10)

    result = extracting_root(num1, k1, m1)

    print(f'Number = {num1}')
    print(f'Write {k1} times')
    print(f'root of degree {m1}')

    print(f'result of expression = {result:.3f}')
