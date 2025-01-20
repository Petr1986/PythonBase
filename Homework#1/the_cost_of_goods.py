"""The cost of the product in kopecks C is known.
Find the cost in rubles r and kopecks k"""

#Функция для вычисления цены
def cost(k: int) -> tuple[int, int]:
    ruble = k // 100
    kopeck = k % 100
    return ruble, kopeck

if __name__ == "__main__":

#Ввод данных
    k1 = int(input("Введите стоимость товара в копейках: "))

#Вычисление цены в рублях и копейках
    price_ruble, price_kopeck = cost(k1)

#Вывод результатов
    print(f'Стоимость товара: {price_ruble} рублей {price_kopeck} копеек.')