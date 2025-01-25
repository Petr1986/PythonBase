"""The last digit of the three-digit number x was subtracted.
When the result was divided by 10,
and the last digit of the number x was added to the quotient on the left,
the result was 237. Find the number x
Based on the fact that the last digit of the number x was added to the quotient
on the left and 237 was obtained, it follows that the last digit of the number
is 2. Consequently, we can replace adding the digit 2
by adding 200. Based on this, we can form the equation
237 = (x-2)/10 + 200"""

def find_number(y) -> float:
    for x in range(10 ** (len(str(y)) - 1), 10 ** len(str(y)) - 1): #Трехзначные числа оканчивающиеся на 2
        modified_number = int(str(x % 10) + str((x - x % 10) // 10))
        if modified_number == y:
            return x

if __name__ == "__main__":

# Ввод данных
    a = int(input('Введите результат выражения: '))

# Выводим ответ
    result = find_number(a)
    print(f'Значение х: {result}')