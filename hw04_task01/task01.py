# -*- coding: utf-8 -*-
import sys

sys.path.append('home/python/samatbek/hw04_task01')

import pack_task01

x = int(raw_input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    print pack_task01.func_1_to_3()
elif 4 <= x <= 6:
    print pack_task01.func_4_to_6(x)
elif 7 <= x <= 9:
    print pack_task01.func_7_to_9(x)
else:
    print pack_task01.func_error()


