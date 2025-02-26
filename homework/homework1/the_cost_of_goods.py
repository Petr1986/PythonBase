"""
The cost of the product in kopecks C is known.
Find the cost in rubles r and kopecks k
"""

import random


def cost(k: int) -> tuple[int, int]:
    min_value = 1
    max_value = 10000
    if k < min_value or k > max_value:
        raise ValueError("The price must be in the range from 1 to 10000")
    ruble = k // 100
    kopeck = k % 100
    return ruble, kopeck


if __name__ == "__main__":

    k1 = random.randint(1, 10000)

    print()

    price_ruble, price_kopeck = cost(k1)

    print(
        f"cost in kopecks = {k1}",
        f"Cost of goods: {price_ruble} rubles {price_kopeck} kopecks.",
        sep="\n",
    )
