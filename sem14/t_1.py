"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
This must stay.
"""
from string import ascii_letters


def filter_ASKII_spaces(text: str):

    tmp = ascii_letters + " "
    out = ""
    for itm in text:
        if itm in tmp:
            out += itm
    out = out.lower()
    return out


if __name__ == '__main__':
    filter_ASKII_spaces(__doc__)
