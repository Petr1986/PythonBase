import random


def count_coin_combination(a1: int, a2: int, a3: int, a4: int, s: int) -> list:
    if not all(1 <= a <= 10 for a in (a1, a2, a3, a4)) or not 20 <= s <= 100:
        raise ValueError("out of range")
    coins = [1, 2, 5, 10]

    counts = [a1, a2, a3, a4]

    combinations = []
    for c1 in range(counts[0] + 1):
        for c2 in range(counts[1] + 1):
            for c3 in range(counts[2] + 1):
                for c4 in range(counts[3] + 1):
                    total = (
                        c1 * coins[0] + c2 * coins[1] + c3 * coins[2] + c4 * coins[3]
                    )
                    if total == s:
                        combinations.append((c1, c2, c3, c4))
    return combinations


if __name__ == "__main__":

    a_1 = random.randint(1, 10)
    a_2 = random.randint(1, 10)
    a_3 = random.randint(1, 10)
    a_4 = random.randint(1, 10)
    s_1 = random.randint(20, 100)

    result = count_coin_combination(a_1, a_2, a_3, a_4, s_1)
    print(a_1, a_2, a_3, a_4)
    print(f"For price: {s_1}")
    print(result)

    # for combo in result:
    # print(f"Coins of 1 rub.: {combo[0]}, coins of 2 rub.: {combo[1]}, coins of 5 rub.: {combo[2]}, coins of 10 rub.: {combo[3]}")
