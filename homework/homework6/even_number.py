import random


def even_number(num: int) -> tuple[list, str]:
    if not 1 <= num <= 5:
        raise ValueError("out of range")
    count = 0
    lst = []
    for i in range(num):
        x = random.randint(1, 50)
        lst.append(x)
        if x % 2 == 0:
            count += 1
    if count > 0:
        return lst, "There are even ones"
    else:
        return lst, "There are no even ones"


if __name__ == "__main__":

    num1 = random.randint(1, 5)

    result = even_number(num1)

    print(f"For {num1}, numbers {result[0]}, {result[1]}")
