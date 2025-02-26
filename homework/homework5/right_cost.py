import random


def ruble_cost(ruble: float) -> str:
    if not 0 <= ruble <= 100:
        raise ValueError("out of range")
    if 11 <= int(ruble) % 100 <= 19:
        return "рублей"
    last_digit = int(ruble) % 10
    if last_digit == 1:
        return "рубль"
    if 2 <= last_digit <= 4:
        return "рубля"
    else:
        return "рублей"


def kopeck_cost(ruble: float) -> str:
    if not 0 <= ruble <= 100:
        raise ValueError("out of range")
    kopeck = round((ruble - int(ruble)) * 100)
    if 11 <= kopeck % 100 <= 19:
        return "копеек"
    last_digit = kopeck % 10
    if last_digit == 1:
        return "копейка"
    if 2 <= last_digit <= 4:
        return "копейки"
    else:
        return "копеек"


if __name__ == "__main__":

    rub = round(random.uniform(1, 100), 2)

    result = (ruble_cost(rub), kopeck_cost(rub))

    print(
        f"for {rub}: {int(rub)} {result[0]} {round((rub - int(rub)) * 100)} {result[1]}"
    )
