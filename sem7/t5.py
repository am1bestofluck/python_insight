"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
from t4 import main
from os import  chdir
from random import  choice

def main_(exts = [".gpg",".dll",",bin"]):
    chdir("t5")
    for i in exts:
        main(extention=i,file_count=choice(range(1,10)))

if __name__ == '__main__':
    main_()