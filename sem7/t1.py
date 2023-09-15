"""
✔Напишите функцию, которая заполняет файл (добавляет в конец)
 случайными парами чисел
. ✔Первое число int, второе - float разделены вертикальной чертой. ✔Минимальное число - -1000,
 максимальное - +1000.
 ✔Количество строк и имя файла передаются как аргументы функции.

"""
from random import choice, uniform


def main(*, lines: int = 10, name: str = "t1_txt.txt"):
    limits,a,b = range(-1000, 1000),-1000,1000
    with open(name, "a") as core:
        for i in range(lines):
            core.write(f"{choice(limits)}|{uniform(a,b)}\n")

    return


if __name__ == '__main__':
    main()
