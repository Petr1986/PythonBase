"""Given two three-digit numbers, find a six-digit number formed
from the two given numbers by adding the second number to the first"""

#Функция для конкатенации строк
def concatenation(first_number: str, second_number: str) -> str:
    return first_number + second_number

if __name__ == "__main__":

#Ввод чисел
    x = input('Введите первое трехзначное число: ')
    y = input('Введите второе трехзначное число: ')

#Получение шестизначного числа
    result = concatenation(x, y)

#Вывод результата
    print('Шестизначное число: ', result)