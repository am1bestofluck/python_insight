"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json
from pathlib import Path


# открываеам файл
def get_input(p: Path) -> 'File':
    with open(p) as f:
        return f.readlines()


# парсим файл
def parse_input(c: list[str]) -> list[tuple[str, str]]:
    out = []
    for line in c:
        tmp = line.strip().split("|")
        try:
            out.append((tmp[0], tmp[1].title()))
        except:
            pass
    return out


# записываем json
def jsonize(c: list[tuple[str, str]]):
    print()
    with open("t1_out.json", "w") as f_o:
        json.dump(c, f_o,indent= 2)
    pass


if __name__ == '__main__':
    a = get_input(Path("../sem7/t3_txt.txt"))
    a = parse_input(a)
    jsonize(a)
