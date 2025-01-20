"""Assign the third digit from the end
of the positive integer to the integer variable h"""

#Функция для определения третьей цифры с конца
def define(num: int) -> int:
    return num % 1000 // 100

if __name__ == "__main__":

#Ввод начального числа
    num1 = int(input('Введите положительное целое число к > 99: '))

#Вариант 1
    third_digit = define(num1)
    print('Третья цифра с конца:', third_digit)

#Вариант 2
# h = str(k)
# print('Третья цифра с конца:', h[-3])