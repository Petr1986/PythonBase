"""Someone decided to hand over empty bottles by packing them in bags,
one bag holds a maximum of k bottles, how many bags will be needed
if the total number of bottles n"""

import random
from math import ceil


def needed_bags(quantity_bottles: int, bottle_in_pack: int) -> int:
    if not 4 <= bottle_in_pack <= 8 or not 20 <= quantity_bottles <= 60:
        raise ValueError("out of range")
    return ceil(quantity_bottles / bottle_in_pack)


if __name__ == "__main__":

    k = random.randint(4, 8)
    n = random.randint(20, 60)

    print(f"number of bottles in a package = {k}")
    print(f"number of bottles = {n}")

    result = needed_bags(n, k)

    print(f"needed {result} backs")
