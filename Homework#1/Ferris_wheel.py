'''В парке развлечений стоит колесо обозрения с четным числом кабинок.
Когда внизу находится кабина №А, то наверху - №В (A < B, А и В одинаковой четности).
Сколько кабинок в колесе обозрения?'''

if __name__ == "__main__":

    #Ввод данных
    a,b = map(int, input('Введите через пробел № кабинок А и В: ').split())

    # Поскольку кабинки располагаются на равном удалении друг от друга,
    # то вычитая из большего номера (кабинка В) меньший номер (кабинка А),
    # мы получаем число равное половине количества кабинок
    quantity = (b - a) * 2

    #Вывод результатов
    print('Количество кабинок в колесе обозрения равно:', quantity)