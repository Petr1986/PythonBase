import random


def cell_color(x: int, y: int) -> str:
    if not all(1 <= num <= 8 for num in (x, y)):
        raise ValueError("out of range")
    if y % 2 == 0 and x % 2 != 0 or y % 2 != 0 and x % 2 == 0:
        return "white"
    else:
        return "black"


if __name__ == "__main__":

    x1 = random.randint(1, 8)
    y1 = random.randint(1, 8)

    result = cell_color(x1, y1)

    print(f"for a cell with coordinate {x1,y1}", f"color {result}", sep="\n")
