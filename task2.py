# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.


def main():  # Получает число и выводит полученный результат
    input_money = get_money()
    usd_money = exchange(input_money)
    print("Ты ввёл int:", input_money, "KZT")
    print("Конвертированная сумма в USD: ", usd_money[0])
    print("Конвертированная сумма в EUR: ", usd_money[1])
    print("Конвертированная сумма в CHF: ", usd_money[2])
    print("Конвертированная сумма в GBP: ", usd_money[3])
    print("Конвертированная сумма в CNY: ", usd_money[4])


def get_money():  # Получает на вход число
    input_data = input("Введи число: ")
    return input_data


def exchange(money):  # Конвертирует полученную сумму
    kzt_list = []
    kzt_to_list = [426.4, 502.42, 463.02, 589.11, 65.97]

    for i in range(len(kzt_to_list)):
        kzt_list.append(int(money) / kzt_to_list[i])
    return kzt_list


main()
