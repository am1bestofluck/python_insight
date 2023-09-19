import json,csv
from pathlib import Path


def get_data(p: Path) -> dict:
    with open(p, encoding="UTF-8", mode="r") as f:
        return json.load(f)


def convert(f):
    headers = "permissions", "id", "name"
    with open('t3_out.csv', 'w', newline='') as f_o:
        csv_write = csv.writer(f_o, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(headers)
        for i,line in enumerate(f):
            csv_write.writerow((line,list(f[line][0].keys())[0],list(f[line][0].values())[0]))


if __name__ == '__main__':
    a = get_data(Path("user_db.json"))
    convert(a)
