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
import logging
from pathlib import Path
from typing import Callable


def arg_parse() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument('arg_path', metavar='path', nargs=1)
    return Path(parser.parse_args().arg_path[0])


def log_path(dst: Path):
    def inner(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal dst
            logging.basicConfig(filename=dst, filemode="at", encoding="utf-8",
                                level=logging.INFO)
            out: namedtuple = func(*args)
            # pdb.set_trace()
            logging.info(str(out._asdict()))

        return wrapper

    return inner


@log_path(Path("t6_log.log"))
def describe_obj(path: Path) -> namedtuple:
    FileSpecs = namedtuple(typename="FileSpecs",
                           field_names="name  extension is_dir_ parent_folder")
    # pdb.set_trace()
    tmp_ = path.absolute()
    name_ = tmp_.stem if tmp_.is_file() else tmp_.parts[-1]
    extension_ = tmp_.suffix if tmp_.is_file() else None
    is_dir__ = tmp_.is_dir()
    # pdb.set_trace()
    try:
        parent_ = tmp_.parts[-2]
    except IndexError:
        parent_ = None
    return FileSpecs(name=name_, extension=extension_, is_dir_=is_dir__,
                     parent_folder=parent_)


if __name__ == '__main__':
    import pdb

    tmp = arg_parse()
    describe_obj(tmp)
