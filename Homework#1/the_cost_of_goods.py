"""Известна стоимость товара в копейках С.
Найти стоимость в рублях r и копейках к"""

if __name__ == "__main__":

#Ввод данных
    k = int(input("Введите стоимость товара в копейках: "))

#Вычисление количества рублей
    r = k // 100

#Вычисление остатка в копейках
    remainder = k % 100

#Вывод результатов
    print(f'Стоимость товара: {r} рублей {remainder} копеек.')