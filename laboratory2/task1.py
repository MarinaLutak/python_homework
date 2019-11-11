"""
Обчислення суми
"""

from validators.validators_library import validator
from validators.validators_library import re_float
from validators.validators_library import re_plus_int

x= float(validator(re_float, 'Введiть значення x'))
n= int(validator(re_plus_int, 'Введiть значення верхньої границi суми (лише натуральнi числа)'))

n = 0
for i in range(0, n + 1):
    n += (x + i) / x ** 2
print(n)