"""
The temperature value in degrees Celsius is given.
Determine the value of the same temperature in degrees Fahrenheit,
if the temperature in Celsius ТС and the temperature in Fahrenheit TF
are related by the following relationship: TC = (TF - 32) * 5 / 9
"""

import random


def conversion(celsius: int) -> float:
    min_value = -273
    max_value = 1000
    if celsius < min_value or celsius > max_value:
        raise ValueError("Temperature should be in the range from -273 to 1000")
    return int((celsius * 9 / 5) + 32)


if __name__ == "__main__":

    celsius_1 = random.randint(-273, 1000)

    fahrenheit = conversion(celsius_1)

    print(
        f"Temperature in Celsius: {celsius_1}",
        f"Temperature in Fahrenheit = {fahrenheit}",
        sep="\n",
    )
