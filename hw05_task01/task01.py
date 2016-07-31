# -*- coding: utf-8 -*-
x = int(raw_input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    string = raw_input("Введите строку: ")
    number = int(raw_input("Введите число повторов строки: "))
    print ((string + "\n") * number)
elif 4 <= x <= 6:
    power = int(raw_input("В какую степеть восвести ваше число? "))
    print x ** power
elif 7 <= x <= 9:
    # -------------------------------------------------------------------
    output_numbers = [i for i in range(x + 1, x + 11)]
    # -------------------------------------------------------------------
    for i in output_numbers:
        print i
else:
    print('Ошибка ввода')


