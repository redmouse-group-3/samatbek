# -*- coding: utf-8 -*-
class IfNum:
    x = 0

    def __init__(self, x):
        self.x = x
        if 9 >= self.x >= 7:
            print self.func_7_to_9()
        elif self.x >= 4:
            print self.func_4_to_6()
        elif self.x >= 1:
            print self.func_1_to_3()
        else:
            print self.func_error()

    def func_1_to_3(self):
        string = raw_input("Введите строку: ")
        number = int(raw_input("Введите число повторов строки: "))
        return (string + "\n") * number

    def func_4_to_6(self):
        power = int(raw_input("В какую степеть восвести ваше число? "))
        return self.x ** power

    def func_7_to_9(self):
        return [i for i in range(self.x + 1, self.x + 11)]

    def func_error(self):
        return 'Ошибка ввода'


x = int(raw_input("Введите число от 1 до 9: "))
num1 = IfNum(x)
