"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
from pathlib import Path
from shutil import move as mv
try:
    from timeout_1 import main as m_tm1, DIR_NAME as fld1, DIR_NAME_ as fld2, cd, md
    from t5 import EXTS
except ImportError:
    from .timeout_1 import main as m_tm1, DIR_NAME as fld1, DIR_NAME_ as fld2, cd, md
    from .t5 import EXTS



def main(folder_to_sort:Path):
    nature = {
        "vid": {EXTS[3]}, "img": {EXTS[0]}, "docs": {EXTS[-1], EXTS[-3]}, "music": {EXTS[-2]}
    }
    cd(folder_to_sort)
    for key_ in nature:
        try:
            md( key_)
        except FileExistsError:
            pass
    for i in os.listdir():
        if Path(i).is_dir():
            continue
        for type_ in nature:
            if Path(i).suffix in nature[type_]:
                mv(i, Path(type_))


if __name__ == '__main__':
    m_tm1()
    main(Path("."))
