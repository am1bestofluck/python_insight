"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
from pathlib import Path
from shutil import move as mv
from timeout_1 import main as m_tm1, DIR_NAME, cd, md
from t5 import EXTS

fold = "timeout2"


def main():
    nature = {
        "vid": {EXTS[3]}, "img": {EXTS[0]}, "docs": {EXTS[-1], EXTS[-3]}, "music": {EXTS[-2]}
    }
    for key_ in nature:
        try:
            md(Path(DIR_NAME)/"fold"/key_)
        except FileExistsError:
            pass
    m_tm1(fold)
    print()
    for i in os.listdir():
        for type_ in nature:
            if Path(i).suffix in nature[type_]:
                mv(i, Path(type_))


if __name__ == '__main__':
    main()
