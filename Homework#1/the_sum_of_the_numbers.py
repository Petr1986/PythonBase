"""Given a three-digit integer. Using // and %,
find the sum of its digits"""


# Функция для вычисления суммы цифр
def calculation(x: int) -> int:
    return x // 100 + x % 100 // 10 + x % 10

if __name__ == "__main__":

#Ввод данных
    num = int(input('Введите целое, трехзначное число: '))

#Подсчет суммы цифр
    result = calculation(num)

#Вывод результатов
    print(f'Сумма цифр числа {num}, равна: {result}')