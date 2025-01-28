"""Four integer variables are entered from the keyboard: a, b, c, d, not equal to 0.
Calculate the value of the expression y = 3ab - 4 / (c * d)"""
import random


def calculation (a: int, b: int, c: int, d: int) -> float:
    return 3 * a * b - 4 / (c * d)

if __name__ == "__main__":

    while True:
        a1 = random.randint(-100, 100)
        b1 = random.randint(-100, 100)
        c1 = random.randint(-100, 100)
        d1 = random.randint(-100, 100)

        if a1 != 0 and b1 != 0 and c1 != 0 and d1 != 0:
            break

    y = calculation(a1, b1, c1, d1)

    print(f'Result of the expression "y = 3ab - 4 / (c * d)": {y:.2f}')
