# -*- coding: utf-8 -*-
class Age:
    age = 1

    def __init__(self, age):
        self.age = age
        if 60 <= self.age < 120:
            print self.func_60_to_120()
        elif 25 <= self.age:
            print self.func_25_to_60()
        elif 18 <= self.age:
            print self.func_18_to_25()
        elif 7 <= self.age:
            print self.func_7_to_18()
        if 0 < self.age:
            print self.func_0_to_7()
        else:
            print self.func_error()

    @staticmethod
    def func_0_to_7():
        return 'Вам в детский сад'

    @staticmethod
    def func_7_to_18():
        return 'Вам в школу'

    @staticmethod
    def func_18_to_25():
        return 'Вам в профессиональное учебное заведение'

    @staticmethod
    def func_25_to_60():
        return 'Вам на работу'

    @staticmethod
    def func_60_to_120():
        return 'Вам предоставляется выбор'

    @staticmethod
    def func_error():
        return 'Вы ввели неправильные данные'

print('Общество в начале XXI века')
age = int(raw_input("Сколько вам лет? "))

object1 = Age(age)
