"""
Знаходження вартості покупки в магазині:
а) вартість однієї покупки з 300 г цукерок і 400 г печива;
б) вартість трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок.
"""

from validators.validators_library import validator
from validators.validators_library import re_plus_float


x= float(validator(re_plus_float, 'Введіть ціну за 1 кг цукерок'))
y= float(validator(re_plus_float, 'Введіть ціну за 1 кг печива'))

print('Вартість однієї покупки з 300 г цукерок і 400 г печива')
V= 0.3*x + 0.4*y
print(V)
print('Вартість трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок')
S= 3*(2*x + 1.8*y)
print(S)