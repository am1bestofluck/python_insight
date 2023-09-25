"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import csv
from pathlib import Path
import pickle

from pprint import pp

IO = {"i": Path("t4_out.pickle"), "o": Path("t4_out.csv")}


def pickle_to_csv(path_i: Path, path_o: Path):
    with( open(path_i, "rb") as io_i,
          open(path_o, "wt",encoding="utf-8") as io_o):
        temp: dict[str, dict] = pickle.loads(io_i.read())

        pp(temp)
        keys_ = [key_ for key_ in temp[[*temp.keys()][0]]]
        header = ["hash"]
        header.extend(keys_)
        to_csv = csv.writer(io_o,lineterminator="\n")
        to_csv.writerow(header,)
        for key_ in temp:
            to_csv.writerow((key_, temp[key_][header[1]],
                             temp[key_][header[2]],
                             temp[key_][header[3]].strip()))


if __name__ == '__main__':
    pickle_to_csv(IO["i"], IO["o"])
