"""
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from string import ascii_lowercase
from random import choice, choices

VOWELS = "aeiouy"
SIZE = range(3, 7)


def line_():
    global VOWELS, SIZE
    for i in range(10):
        yield f"{choice(VOWELS)[0].upper()}{''.join(choices(ascii_lowercase, k=choice(SIZE)))}\n"


def main():
    with open("t2_txt.txt","xt") as core:
        lines = iter(line_())
        while True:
            try:
                core.write(next(lines))
            except:
                return


if __name__ == '__main__':
    main()
