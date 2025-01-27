"""The temperature value in degrees Celsius is given.
Determine the value of the same temperature in degrees Fahrenheit,
if the temperature in Celsius ТС and the temperature in Fahrenheit TF
are related by the following relationship: TC = (TF - 32) * 5 / 9"""

import random

def conversion(x: int) -> float:
    return (x * 9 / 5) + 32

if __name__ == "__main__":

    celsius = random.randint(-30,50)

    fahrenheit = conversion(celsius)

    print("Температура по фаренгейту =", int(fahrenheit))