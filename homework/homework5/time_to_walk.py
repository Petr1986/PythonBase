import random


def time_to_walk(temperature_b: float, temperature: int, weather: str) -> str:
    if not 36 <= temperature_b <= 37 or not -20 <= temperature <= 32:
        raise ValueError("out of range")
    if 36 <= temperature_b <= 36.8:
        if -15 <= temperature <= 28:
            if weather in ("worm", "sunny"):
                return "go walk"
            else:
                return "The weather is bad"
        else:
            return "Extremal temperature"
    else:
        return " Temperature of body is too high"


if __name__ == "__main__":

    weat1 = ["cloudy", "snow", "worm", "sunny"]

    temp = random.randint(-20, 32)
    temp_b = random.uniform(36, 37)
    weat = random.choice(weat1)

    result = time_to_walk(temp_b, temp, weat)

    print(
        f"If temperature of body {temp_b:.1f}, temperature outside {temp} and the weather is {weat}",
        result,
        sep="\n",
    )
