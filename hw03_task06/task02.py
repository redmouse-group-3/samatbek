# -*- coding: utf-8 -*-
from package01 import if_module02

print('Общество в начале XXI века')
age = int(raw_input("Сколько вам лет? "))

if 0 < age < 7:
    print if_module02.func_0_to_7()
elif 7 <= age < 18:
    print if_module02.func_7_to_18()
elif 18 <= age < 25:
    print if_module02.func_18_to_25()
elif 25 <= age < 60:
    print if_module02.func_25_to_60()
elif 60 <= age < 120:
    print if_module02.func_60_to_120()
else:
    print if_module02.func_error()
