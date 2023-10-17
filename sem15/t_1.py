"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging
from pathlib import Path


def err_log(output: Path):
    logging.basicConfig(filename=output, filemode="at", encoding="utf-8")
    try:
        raise ZeroDivisionError("it's ok")
    except ZeroDivisionError as e:
        logging.error(e.args)


if __name__ == '__main__':
    err_log(Path("t1_log.log"))
