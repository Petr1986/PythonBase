"""The temperature value in degrees Celsius is given.
Determine the value of the same temperature in degrees Fahrenheit,
if the temperature in Celsius ТС and the temperature in Fahrenheit TF
are related by the following relationship: TC = (TF - 32) * 5 / 9"""

import random


def conversion(x: int) -> float:
    if not -273 <= x <= 1000:
        raise ValueError(f"Temperature {x} is out of range")
    return int((x * 9 / 5) + 32)


if __name__ == "__main__":

    celsius = random.randint(-273, 1000)
    print(f"Temperature in Celsius: {celsius}")

    fahrenheit = conversion(celsius)

    print("Temperature in Fahrenheit =", int(fahrenheit))
