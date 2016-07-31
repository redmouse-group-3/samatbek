# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractAttribute:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, x=0):
        self.x = x


class Methods:
    def __init__(self):
        pass

    @staticmethod
    def func_1_to_3():
        string = raw_input("Введите строку: ")
        number = int(raw_input("Введите число повторов строки: "))
        return (string + "\n") * number

    @staticmethod
    def func_4_to_6(x):
        power = int(raw_input("В какую степеть восвести ваше число? "))
        return x ** power

    @staticmethod
    def func_7_to_9(x):
        return [i for i in range(x + 1, x + 11)]

    @staticmethod
    def func_error():
        return 'Ошибка ввода'


class IfNum(AbstractAttribute, Methods):
    def __init__(self, x):
        super(IfNum, self).__init__(x)
        if 9 >= self.x >= 7:
            print self.func_7_to_9(self.x)
        elif self.x >= 4:
            print self.func_4_to_6(self.x)
        elif self.x >= 1:
            print self.func_1_to_3()
        else:
            print self.func_error()


x = int(raw_input("Введите число от 1 до 9: "))
num1 = IfNum(x)
