"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

"""

import json, csv
from pathlib import Path
try:
    from t_2 import PATH
except ImportError:
    from .t_2 import PATH

CSV_OUT = 't3_out.csv'


def get_data(p: Path) -> dict:
    with open(p, encoding="еUTF-8", mode="r") as f:
        return json.load(f)


def convert(f):
    headers = "permissions", "id", "name"
    with open(CSV_OUT, 'w', newline='') as f_o:
        csv_write = csv.writer(f_o, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(headers)
        for permissions in f:
            for id in f[permissions]:
                csv_write.writerow([permissions, id, f[permissions][id]])


def main(p: Path):
    a = get_data(Path(p))
    convert(a)


if __name__ == '__main__':
    main(PATH)
