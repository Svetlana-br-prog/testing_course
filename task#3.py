from task2 import exchange
# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
# 3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.


while True:
    input_data = input("Введите новое число: ")

    if len(input_data) == 0:
        print("Вы ввели пустое поле. Введите число.")
    else:
        try:
            if int(input_data) <= 0:
                print("Введите положительное число.")
            else:
                usd_money = exchange(input_data)
                print("Ты ввёл int:", input_data, "KZT")
                print("Конвертированная сумма в USD: ", usd_money[0])
                print("Конвертированная сумма в EUR: ", usd_money[1])
                print("Конвертированная сумма в CHF: ", usd_money[2])
                print("Конвертированная сумма в GBP: ", usd_money[3])
                print("Конвертированная сумма в CNY: ", usd_money[4])
                break
        except ValueError:
            print("Вы ввели не число. Введите число.")