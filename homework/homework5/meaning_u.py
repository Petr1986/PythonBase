import random


def meaning_u(x: float, y: float, z: float) -> str | float:
    if not all(-20 <= num <= 20 for num in (x, y, z)):
        raise ValueError("out of range")
    if x + y - z == 0:
        return "You can't divide by zero"
    else:
        return round((max(x, y, z) + min(x, y, z)) / (x + y - z), 2)


if __name__ == "__main__":

    x1 = random.uniform(-20, 20)
    y1 = random.uniform(-20, 20)
    z1 = random.uniform(-20, 20)

    result = meaning_u(x1, y1, z1)

    if isinstance(result, str):
        print(result)

    else:
        print(f"For x = {x1:.2f}, y = {y1:.2f}, z = {z1:.2f}, u = {result}")
