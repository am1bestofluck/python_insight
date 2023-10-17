"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import argparse
from collections import namedtuple
from pathlib import Path


def arg_parse() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument('arg_path', metavar='path', nargs=1)
    # pdb.set_trace()
    return Path(parser.parse_args().arg_path[0])


def describe_obj(path: Path) -> namedtuple:
    FileSpecs = namedtuple(typename="FileSpecs", field_names="folder_file parent_folder")
    pdb.set_trace()
    return  FileSpecs(path.suffix,path.parts)

if __name__ == '__main__':
    import pdb
    tmp = arg_parse()
    describe_obj(tmp)