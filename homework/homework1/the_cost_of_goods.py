"""The cost of the product in kopecks C is known.
Find the cost in rubles r and kopecks k"""

import random


def cost(k: int) -> tuple[int, int]:
    if not 1 <= k <= 10000:
        raise ValueError("out of rage")
    ruble = k // 100
    kopeck = k % 100
    return ruble, kopeck


if __name__ == "__main__":

    k1 = random.randint(1, 10000)

    print(f"cost in kopecks = {k1}")

    price_ruble, price_kopeck = cost(k1)

    print(f"Cost of goods: {price_ruble} rubles {price_kopeck} kopecks.")
