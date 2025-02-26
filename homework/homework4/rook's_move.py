import random


if __name__ == "__main__":

    x1 = random.randint(1, 8)
    x2 = random.randint(1, 8)
    y1 = random.randint(1, 8)
    y2 = random.randint(1, 8)

    can_move = x1 == x2 or y1 == y2

    print(f"for move from {x1,y1} to {x2, y2}", can_move, sep="\n")
