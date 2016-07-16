# -*- coding: utf-8 -*-
x = int(raw_input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    s = raw_input("Введите строку: ")
    n = int(raw_input("Введите число повторов строки: "))
    count1 = 0
    while count1 < n:
        print s
        count1 += 1
elif 4 <= x <= 6:
    m = int(raw_input("В какую степеть восвести ваше число? "))
    print x ** m
elif 7 <= x <= 9:
    count2 = 1
    while count2 <= 10:
        print x + count2
        count2 += 1
else:
    print('Ошибка ввода')