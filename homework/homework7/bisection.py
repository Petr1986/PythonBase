import math


def f(x: int):
    return 0.5 * x - 0.5 + math.sin(x)


def bisection(a, b, epsilon):
    if f(a) * f(b) >= 0:
        raise ValueError(
            "The function must take different signs at the ends of the segment"
        )
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            return c
        elif f(a) * f(b) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


if __name__ == "__main__":

    a1, b1 = -1, 1
    epsilon1 = 1e-6

    result = bisection(a1, b1, epsilon1)

    print(f"Approximate root: {result}")
