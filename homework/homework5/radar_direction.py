import random


def radar_direction(current: str, command1: int, command2: int) -> str:
    if not all(-1 <= comm <= 2 and comm != 0 for comm in (command1, command2)):
        raise ValueError("out of range")
    transitions = {
        "north": {1: "west", -1: "east", 2: "south"},
        "east": {1: "north", -1: "south", 2: "west"},
        "south": {1: "east", -1: "west", 2: "north"},
        "west": {1: "south", -1: "north", 2: "east"},
    }
    current = transitions[current][command1]
    current = transitions[current][command2]
    return current


if __name__ == "__main__":

    current1 = random.choice(["north", "east", "south", "west"])
    command_1 = random.choice([1, -1, 2])
    command_2 = random.choice([1, -1, 2])

    result = radar_direction(current1, command_1, command_2)

    print(
        f"initial direction: {current1} command 1: {command_1}, command 2: {command_2}"
    )
    print(f"current direction: {result}")
