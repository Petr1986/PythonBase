"""Given a three-digit integer. Using // and %,
find the sum of its digits"""


def calculation(x: int) -> int:
    return x // 100 + x % 100 // 10 + x % 10

if __name__ == "__main__":

    num = int(input('Введите целое, трехзначное число: '))

    result = calculation(num)

    print(f'Сумма цифр числа {num}, равна: {result}')