def sum_of_cubes() -> list:
    lst = []
    for i in range(100, 1000):
        if i == (i % 1000 // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 10) ** 3:
            lst.append(i)
    return lst


if __name__ == "__main__":

    result = sum_of_cubes()

    print(f"{result}")
