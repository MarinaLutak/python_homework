"""
Обчислення суми непарних чисел в діапазоні вказаному користувачем
"""

from validators.validators_library import validator
from validators.validators_library import re_plus_int

i= int(validator(re_plus_int, 'Введіть значення нижньої границі суми i '))
j= int(validator(re_plus_int, 'Введіть значення верхньої границі суми j '))

sum = 0
for k in range(i, j+1):
    if k%2 != 0:
        sum += k
print(sum)