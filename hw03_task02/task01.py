# -*- coding: utf-8 -*-
def func_1_to_3():
    string = raw_input("Введите строку: ")
    number = int(raw_input("Введите число повторов строки: "))
    print ((string + "\n") * number)


def func_4_to_6():
    power = int(raw_input("В какую степеть восвести ваше число? "))
    print x ** power


def func_7_to_9():
    output_numbers = [i for i in range(x + 1, x + 11)]
    for i in output_numbers:
        print i


def func_error():
    print('Ошибка ввода')

x = int(raw_input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    func_1_to_3()
elif 4 <= x <= 6:
    func_4_to_6()
elif 7 <= x <= 9:
    func_7_to_9()
else:
    func_error()


