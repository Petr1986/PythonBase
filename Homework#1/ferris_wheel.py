"""There is a Ferris wheel with an even number of cabins in an amusement park.
When cabin #A is at the bottom, then cabin #B is at the top (A < B, A and B are of the same parity).
How many cabins are there in the Ferris wheel?"""

#Функция для вычисления количества кабинок
# Поскольку кабинки располагаются на равном удалении друг от друга,
# то вычитая из большего номера (кабинка В) меньший номер (кабинка А),
# мы получаем число равное половине количества кабинок
def quantity(a: int, b: int) -> int:
    return (b - a) * 2

if __name__ == "__main__":

#Ввод данных
    a1, b1 = map(int, input('Введите через пробел № кабинок А и В: ').split())

#Вычисление результата
    result = quantity(a1, b1)

#Вывод результатов
    print('Количество кабинок в колесе обозрения равно:', result)