# -*- coding: utf-8 -*-
def social_status(age):
    if 0 < age <= 7:
        print('Вам в детский сад')
    elif 7 < age <= 18:
        print('Вам в школу')
    elif 18 < age <= 25:
        print('Вам в профессиональное учебное заведение')
    elif 25 < age <= 60:
        print('Вам на пенсию')
    elif 60 < age <= 120:
        print('Вам предоставляется выбор')
    else:
        print('Вы ввели неправильные данные')

print('Общество в начале XXI века')
age = int(raw_input("Сколько вам лет? "))

social_status(age)
