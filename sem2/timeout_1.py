"""
✔ Создайте вручную список с повторяющимися целыми числами.++
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

from random import choices
from os import unlink, startfile

OUT_PATH = "timeout_1_out.txt"


def main(list_size: int):
    global OUT_PATH
    temp = choices(population=range(list_size // 2), k=list_size)
    buffer = set(temp)
    out = []
    for i in range(list_size):
        if temp[i] % 2:
            out.append(i+1)
    try:
        unlink(OUT_PATH)
    except FileNotFoundError:
        pass  # expected behavior
    with open(OUT_PATH, 'x') as flush:
        strfy_i = str(list(enumerate(temp)))
        expected_line_len = 80
        lines_i = len(strfy_i) // expected_line_len+1
        line_i = len(strfy_i) // lines_i
        flush.write("in=")
        flush.writelines([f"{strfy_i[i:i+line_i]}\n" for i in range(0, len(strfy_i), line_i)])
        strfy_o = str(list(out))
        lines_o = len(strfy_o) // expected_line_len+1
        line_o = len(strfy_o) // lines_o
        flush.write("out=")
        flush.writelines([f"{strfy_o[i:i+line_o]}\n" for i in range(0, len(strfy_o), line_o)])
    startfile(OUT_PATH)


if __name__ == '__main__':
    main(100)
