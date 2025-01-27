"""Four integer variables are entered from the keyboard: a, b, c, d, not equal to 0.
Calculate the value of the expression y = 3ab - 4 / (c * d)"""

def calculation (a: int, b: int, c: int, d: int) -> float:
    return 3 * a * b - 4 / (c * d)

if __name__ == "__main__":

    a1, b1, c1, d1 = map(int, input('Введите значения a,b,c,d, через пробел: ').split())

    y = calculation(a1, b1, c1, d1)

    print(f'Результат выражения "y = 3ab - 4 / (c * d)": {y}')