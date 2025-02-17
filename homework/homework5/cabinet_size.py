import random


def cabinet_size(height: int, width: int, height_op: int, width_op: int) -> bool:
    if not all(5 <= num <= 100 for num in (height, width, height_op, width_op)):
        raise ValueError("out of range")
    return (
        height <= height_op
        and width <= width_op
        or height <= width_op
        and width <= height_op
    )


if __name__ == "__main__":

    h = random.randint(5, 100)
    w = random.randint(5, 100)
    h1 = random.randint(5, 100)
    w1 = random.randint(5, 100)

    print(f"for cabinet size {h, w} and opening size {h1,w1}")

    result = cabinet_size(h, w, h1, w1)

    print(result)
