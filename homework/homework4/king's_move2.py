import random


if __name__ == "__main__":

    x1 = random.randint(1, 8)
    x2 = random.randint(1, 8)
    y1 = random.randint(1, 8)
    y2 = random.randint(1, 8)

    result = True

    if not abs(x1 - x2) == 1 or not abs(y1 - y2) == 1:
        result = False

    print(f"for move from {x1, y1} to {x2, y2}", result, sep="\n")
