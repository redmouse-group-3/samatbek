# -*- coding: utf-8 -*-
import sys

sys.path.append('home/python/samatbek/hw04_task01')

import pack_task02

print('Общество в начале XXI века')
age = int(raw_input("Сколько вам лет? "))

if 120 > age >= 60:
    print pack_task02.func_60_to_120()
elif age >= 25:
    print pack_task02.func_25_to_60()
elif age >= 18:
    print pack_task02.func_18_to_25()
elif age >= 7:
    print pack_task02.func_7_to_18()
elif age > 0:
    print pack_task02.func_0_to_7()
else:
    print pack_task02.func_error()
