"""Four integer variables are entered from the keyboard: a, b, c, d, not equal to 0.
Calculate the value of the expression y = 3ab - 4 / (c * d)"""
import random


def calculation (a: int, b: int, c: int, d: int) -> float:
    if all(-100 <= x <= 100 for x in(a,b,c,d)):
        raise ValueError('out of range')
    return 3 * a * b - 4 / (c * d)

if __name__ == "__main__":

    a1 = random.randint(-100, -1) if random.random() < 0.5 else random.randint(1, 100)
    b1 = random.randint(-100, -1) if random.random() < 0.5 else random.randint(1, 100)
    c1 = random.randint(-100, -1) if random.random() < 0.5 else random.randint(1, 100)
    d1 = random.randint(-100, -1) if random.random() < 0.5 else random.randint(1, 100)

    print(f'integer a = {a1}')
    print(f'integer b = {b1}')
    print(f'integer c = {c1}')
    print(f'integer d = {d1}')

    y = calculation(a1, b1, c1, d1)

    print(f'Result of the expression "y = 3ab - 4 / (c * d)": {y:.2f}')
