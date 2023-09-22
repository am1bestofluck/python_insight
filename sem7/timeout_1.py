"""
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
try:
    from t5 import main_ as m_i, EXTS, DIR_NAME_
except ImportError:
    from .t5 import main_ as m_i, EXTS, DIR_NAME_
from pathlib import Path
from os import chdir as cd, mkdir as md

DIR_NAME = "t6_f"


def main(folder: str = DIR_NAME, extensions: list[str] = EXTS):
    "в folder ложим всякую рандоную чушь, c расширениями extensions"
    path_ = Path(folder)
    if not path_.exists():
        md(path_)
    cd(path_)
    m_i(extensions)


if __name__ == '__main__':
    main()
