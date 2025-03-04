import math
import random


def dms_to_radian(
    degrees: int, minutes: int, seconds: int
) -> tuple[float, float, float, float]:
    min_value_deg = 0
    max_value_deg = 360
    min_value_time = 1
    max_value_time = 59
    for x in (minutes, seconds):
        if x < min_value_time or x > max_value_time:
            raise ValueError("Minutes and seconds must be between 1 and 59")
    if degrees < min_value_deg or degrees > max_value_deg:
        raise ValueError("Degrees can range from 0 to 360")
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    rad = decimal_degrees * (math.pi / 180)
    return (
        round(rad, 2),
        round(math.sin(rad), 2),
        round(math.cos(rad), 2),
        round(math.tan(rad), 2),
    )


if __name__ == "__main__":

    deg = random.randint(0, 360)  # int(input("Введите градусы угла: "))
    minute = random.randint(1, 59)  # int(input("Введите минуты угла: "))
    second = random.randint(1, 59)  # int(input("Введите секунды угла: "))

    result = dms_to_radian(deg, minute, second)

    print(
        f"{deg} d {minute} ' {second} '' = {result[0]:.2f} radian",
        f"sin({deg} d {minute} ' {second} '') = {result[1]:.2f}",
        f"cos({deg} d {minute} ' {second} '') = {result[2]:.2f}",
        f"tan({deg} d {minute} ' {second} '') = {result[3]:.2f}",
        sep="\n",
    )
