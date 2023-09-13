"""
Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные
 в модуль функции под псевдонимами. (3-7 строк импорта).
"""

from fractions import Fraction as Fr
from math import floor as bot, ceil as top, pow as self_mult
from sys import argv as console, exit as q


def main():
    if len(console) != 3:
        q(1)
    print(
        Fr(self_mult(
            (Fr(float(console[1]))-bot(float(console[1])) *
             Fr(float(console[2]))-top(float(console[2]))
             ), 2
        ))
    )


if __name__ == '__main__':
    main()
