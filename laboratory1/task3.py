"""
Обчислення функції, в залежності від введеного значення х
"""
from validators.validators_library import validator
from validators.validators_library import re_float

x= float(validator(re_float, 'Введіть аргумент функції:'))

if x<=7:
    print(-3*x+9)
else:
    print(1/(x-7))