import random


def find_intersection(
    x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int
) -> tuple[int, int, int, int] | str:
    if not all(0 <= n <= 50 for n in (x1, y1, x2, y2)) and not all(
        1 <= j <= 20 for j in (w1, h1, w2, h2)
    ):
        raise ValueError("out of range")
    x_min = max(x1, x2)
    y_min = max(y1, y2)
    x_max = min(x1 + w1, x2 + w2)
    y_max = min(y1 + h1, y2 + h2)
    if x_min < x_max and y_min < y_max:
        return x_min, y_min, x_max, y_max
    else:
        return "the rectangles do not intersect"


if __name__ == "__main__":

    x_1 = random.randint(0, 50)
    y_1 = random.randint(0, 50)
    h_1 = random.randint(1, 20)
    w_1 = random.randint(1, 20)
    x_2 = random.randint(0, 50)
    y_2 = random.randint(0, 50)
    h_2 = random.randint(1, 20)
    w_2 = random.randint(1, 20)

    result = find_intersection(x_1, y_1, h_1, w_1, x_2, y_2, h_2, w_2)

    print(
        f"Rectangle 1: Bottom-left corner: ({x_1}, {y_1}), Width: {w_1}, Height: {h_1}"
    )
    print(
        f"Rectangle 2: Bottom-left corner: ({x_2}, {y_2}), Width: {w_2}, Height: {h_2}"
    )
    print(result)
