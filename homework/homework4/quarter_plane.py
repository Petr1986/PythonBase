import random


def quarter_plane(x: int, y: int) -> str:
    if not all(-20 <= num <= 20 for num in (x, y)):
        raise ValueError("out of range")
    if x > 0 and y > 0:
        return "first quarter"
    elif x < 0 < y:
        return "second quarter"
    elif x < 0 and y < 0:
        return "third quarter"
    elif y < 0 < x:
        return "fourth quarter"
    elif y == 0:
        return "point on axis y"
    elif x == 0:
        return "point on axis x"
    else:
        return "origin of coordinates"


if __name__ == "__main__":

    x1 = random.randint(-20, 20)
    y1 = random.randint(-20, 20)

    result = quarter_plane(x1, y1)

    print(f"A point with coordinate {x1,y1}", f"lines {result}", sep="\n")
