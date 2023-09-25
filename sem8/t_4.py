"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import csv
import json
from hashlib import md5
from pathlib import Path
from pprint import pp

from t_3 import CSV_OUT

T4_OUT = Path("t4_out.json")


def hash_function(id: str, name: str):
    return md5(bytes(f"{id}{name}", "utf-8")).hexdigest()


def touch_points(i: Path, o: Path):
    for_json = dict()
    with (open(i, "r") as file_i,
          open(o, "w") as file_o):
        csv_content = csv.reader(file_i)

        for line in list(csv_content)[1:]:
            permission, id, name = line[0].split()
            buffer_id = str(id).zfill(10)
            buffer_name = name.title()
            key_ = hash_function(buffer_id, buffer_name)
            for_json[key_] = {"permission": permission, "id": buffer_id, "name": buffer_name}

        file_o.write(json.dumps(for_json,indent=1))



if __name__ == '__main__':
    touch_points(i=Path(CSV_OUT), o=T4_OUT)
