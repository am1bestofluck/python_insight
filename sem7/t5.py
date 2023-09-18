"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
from t4 import main
from os import chdir, mkdir
from random import choice

EXTS = (".gpg", ".dll", ".bin", ".mp4", ".docx", ".mp3", ".rtf")
DIR_NAME_ = "t5"


def main_(exts: list[str] = EXTS):
    global EXTS, DIR_NAME_
    try:
        chdir(DIR_NAME_)
    except FileNotFoundError:
        mkdir(DIR_NAME_)
        chdir(DIR_NAME_)
    for i in exts:
        main(extention=i, file_count=choice(range(1, 10)))


if __name__ == '__main__':
    main_()
