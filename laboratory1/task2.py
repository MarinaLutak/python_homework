"""
Знаходження розташування точки на площині ХОY
"""
from validators.validators_library import validator
from validators.validators_library import re_float

x= float(validator(re_float, 'На площині задано точку А(x;y). Введіть значення x:'))
y= float(validator(re_float, 'Введіть значення y:'))

if x>0 and y>0:
    print('Точка розташована у першій координатній чверті')
if x>0 and y<0:
    print('Точка розташована у четвертій координатній чверті')
if x<0 and y>0:
    print('Точка розташована у другій координатній чверті')
if x<0 and y<0:
    print('Точка розташована у третій координатній чверті')
if x==0 and y!=0:
    print('Точка розташована на осі OY')
if x!=0 and y==0:
    print('Точка розташована на осі OX')
if x==0 and y==0:
    print('Точка розташована у початку координат')