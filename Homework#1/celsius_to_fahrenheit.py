"""The temperature value in degrees Celsius is given.
Determine the value of the same temperature in degrees Fahrenheit,
if the temperature in Celsius ТС and the temperature in Fahrenheit TF
are related by the following relationship: TC = (TF - 32) * 5 / 9"""

#Функция для перевода градусов цельсия в Фаренгейты
def conversion(x: int) -> float:
    return 9 * celsius / 5 + 32

if __name__ == "__main__":

#Ввод данных
    celsius = int(input('Введите температуру в градусах цельсия:'))

# Перевод градусов цельсия в градусы фаренгейта
    fahrenheit = conversion(celsius)

#Вывод результатов
    print("Температура по фаренгейту =", int(fahrenheit))