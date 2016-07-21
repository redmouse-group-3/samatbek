# -*- coding: utf-8 -*-
def func_0_to_7():
    print('Вам в детский сад')


def func_7_to_18():
    print('Вам в школу')


def func_18_to_25():
    print('Вам в профессиональное учебное заведение')


def func_25_to_60():
    print('Вам на работу')


def func_60_to_120():
    print('Вам предоставляется выбор')


def func_error():
    print('Вы ввели неправильные данные')

print('Общество в начале XXI века')
age = int(raw_input("Сколько вам лет? "))

if 0 < age < 7:
    func_0_to_7()
elif 7 <= age < 18:
    func_7_to_18()
elif 18 <= age < 25:
    func_18_to_25()
elif 25 <= age < 60:
    func_25_to_60()
elif 60 <= age < 120:
    func_60_to_120()
else:
    func_error()
