"""
Видалення символів зі слів
"""

"""
Програма буде видаляти указану кількість символів зі слів, з указаної позиції, за указаною ознакою
"""

from validators.validators_library import validator
from validators.validators_library import re_plus_int


def delete_symbol(text, symbols, count, index):
    """
    Функція видаляє символи зі слів у введеному користувачем тексті,
    :param text:
    :param symbols:
    :param count:
    :param index:
    :return:
    """
    text= text.split()
    i= 0
    while i<len(text):
        word= text[i]
        if word[:-len(symbols)-1: -1]== symbols[::-1]:
            text[i]= word[:index]+word[index+count:]
        i+= 1
    return ' '.join(text)

text= input('Введіть текст: ')
symbols= input('Виедіть символи, на які закінчуються слова, для подальшого їх змінення: ')
count= int(validator(re_plus_int, 'Введіть кількість символів, які бажаєте видалити зі слова: '))
index= int(validator(re_plus_int, 'Введіть позицію (починаючи з 0) з якої бажаєте видалити символи: '))
print(delete_symbol(text, symbols, count, index))