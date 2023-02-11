# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
if month < 1 or month > 12:
    print("Incorrect month")
else:
    print('Вы ввели', month)
    if month in (1, 3, 5, 7, 8, 10, 12):
        print("Month has 31 day")
    elif month in (4, 6, 9, 11):
        print("Month has 30 days")
    else:
        print("Month has 28 days")
