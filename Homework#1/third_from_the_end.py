"""Assign the third digit from the end
of the positive integer to the integer variable h"""

def define(num: int) -> int:
    return num % 1000 // 100

if __name__ == "__main__":

    num1 = int(input('Введите положительное целое число к > 99: '))

    third_digit = define(num1)
    print('Третья цифра с конца:', third_digit)