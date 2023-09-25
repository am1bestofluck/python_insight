"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.

"""

import csv
from pathlib import Path
import pickle
from pprint import pp

from t_6 import IO


def csv_as_pickle(file_i: Path):
    with open(file_i, "r", encoding="utf-8") as io_i:
        content = list(csv.reader(io_i.readlines()))
        temp = {}
        masks = content[0]
        for i in content[1:]:
            temp[i[0]] = {masks[1]: i[1],
                          masks[2]: i[2],
                          masks[3]: i[3]}
        pkl = pickle.dumps(bytes(str(temp), "utf-8"))
        print(pickle.loads(pkl))


if __name__ == '__main__':
    csv_as_pickle(IO["o"])
