# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

def count_m(money, val):  # Конвертирует полученную сумму
    input_money = 0
    v = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
    mon_to_list = [426.4, 502.42, 463.02, 589.11, 65.97]

    for i in range(len(v)):
        if val == v[i]:
            input_money = int(money)/mon_to_list[i]
        else:
            continue
    return input_money


print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")

while True:

    input_val = input("Введи валюту которую выбрал: ").upper()
    input_sum = input("Введите сумму: ")

    if len(input_sum) == 0:
        print("Вы ввели пустое поле. Введите число.")
    else:
        try:
            if int(input_sum) <= 0:
                print("Введите положительное число.")
            else:
                usd_money = count_m(input_sum, input_val)
                print("Вы ввели сумму ", input_sum, " и валюту ", input_val)
                print("конвертированная сумма в ", input_val, " = ", usd_money)
        except ValueError:
            print("Вы ввели не число. Введите число.")
