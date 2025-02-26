import random


def chocolate(slices: int, k_slices: int) -> bool:
    if not 10 <= slices <= 20 or not 5 <= k_slices <= 10:
        raise ValueError("out of range")
    return slices / 2 == k_slices


if __name__ == "__main__":

    slices1 = random.randint(10, 20)
    k_slices1 = random.randint(5, 10)

    result = chocolate(slices1, k_slices1)

    print(
        f"If chocolate consist of pieces {slices1} and K pieces {k_slices1}",
        result,
        sep="\n",
    )
