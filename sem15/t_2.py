"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

"""
import logging
from pathlib import Path
from typing import Callable


def log_output(file_name: Path):
    def save_vals(func: Callable):
        logging.basicConfig(filename=file_name, filemode="at", encoding="utf-8",level=logging.INFO)

        def wrapper(*args, **kwargs):
            out = func(*args, *kwargs)
            logging.info(
                "\n".join([f"{args[0]=}",
                           f"{args[1]=}",
                           f"{out=}",
                           ]))
            return out

        return wrapper

    return save_vals


# @save_vals
@log_output(file_name=Path("t2_log.log"))
def add_lists(a: list[int], b: list[int]) -> list[int]:
    """
    adds values in int lists by indexes
    :param a:
    :param b:
    :return: list[int]
    # >>> add_lists([1,2,3],[4,5,6])
    # [5, 7, 9]
    # >>> add_lists([],[1,2,3])
    # [1, 2, 3]
    """
    c = []
    base = a if len(a) > len(b) else b
    add_ = b if base == a else a
    for i in range(len(base)):
        try:
            c.append(base[i] + add_[i])
        except IndexError:
            c.append(base[i])
    return c


if __name__ == '__main__':
    a = [1, 23, 45, 6]
    b = a
    print(add_lists(a, b))
