import math
import random


def dms_to_radian(
    degrees: int, minutes: int, seconds: int
) -> tuple[float, float, float, float]:
    if not all(1 <= t <= 59 for t in (minutes, seconds)) or not 1 <= degrees <= 180:
        raise ValueError("out of range")
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    rad = decimal_degrees * (math.pi / 180)
    return (
        round(rad, 2),
        round(math.sin(rad), 2),
        round(math.cos(rad), 2),
        round(math.tan(rad), 2),
    )


if __name__ == "__main__":

    deg = random.randint(1, 180)  # int(input("Введите градусы угла: "))
    minute = random.randint(1, 59)  # int(input("Введите минуты угла: "))
    second = random.randint(1, 59)  # int(input("Введите секунды угла: "))

    result = dms_to_radian(deg, minute, second)

    print(f"{deg} d {minute} ' {second} '' = {result[0]:.2f} радиан")

    print(f"sin({deg} d {minute} ' {second} '') = {result[1]:.2f}")
    print(f"cos({deg} d {minute} ' {second} '') = {result[2]:.2f}")
    print(f"tan({deg} d {minute} ' {second} '') = {result[3]:.2f}")
