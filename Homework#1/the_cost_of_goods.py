"""The cost of the product in kopecks C is known.
Find the cost in rubles r and kopecks k"""

import random

def cost(k: int) -> tuple[int, int]:
    ruble = k // 100
    kopeck = k % 100
    return ruble, kopeck

if __name__ == "__main__":

    k1 = random.randint(1, 10000)

    price_ruble, price_kopeck = cost(k1)

    print(f'Стоимость товара: {price_ruble} рублей {price_kopeck} копеек.')