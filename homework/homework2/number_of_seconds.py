
import random


def find_second(sec: int) ->tuple[int, int, int, int]:
    if not 4000 <= sec <= 12000:
        raise ValueError('out of range')
    minutes = sec // 60
    hours = sec // 3600
    sec_from_beginning = sec % 60
    minutes_from_beginning = (sec % 3600) // 60
    return minutes, hours, sec_from_beginning, minutes_from_beginning


if __name__ == "__main__":

    t = random.randint(4000, 12000)

    print(f'number of seconds = {t}\n')

    result = find_second(t)

    print(f'minutes = {result[0]}\nhours = {result[1]}\nseconds since the beginning = {result[2]}\nminutes since the beginning {result[3]}')
