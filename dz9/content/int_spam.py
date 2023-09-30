from copy import deepcopy
from typing import Callable
from random import randint, choices
from pathlib import Path

import csv

try:
    from roots_x_pow2 import roots
    from csv_to_json import json_converter, OUT
except ImportError:
    from .roots_x_pow2 import roots
    from .csv_to_json import json_converter, OUT

FILENAME = Path("rand_ints.csv")
REPETITIONS = randint(100, 1000)
HEADERS = ("a", "b", "c")


def wr_roots(func: Callable):
    def wrapper(*args, **kwargs):
        """нахуя? нахуя? нахуя?"""
        temp = next(iter(func(args[0])))
        a, b, c = temp.values()
        temp.update({"out": roots(a, b, c)})
        return temp

    return wrapper


def repeat(n: int):
    def repeat_deco(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal n
            out: list[dict[str, int]] = []
            for i in range(n):
                out.append(
                    func(args[0])
                )
            return out

        return wrapper

    return repeat_deco


def to_csv(name: Path):
    global HEADERS

    def dump(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal name
            temp = func(args[0])

            with open(name, mode="wt", encoding="utf-8") as core:
                blank = csv.DictWriter(f=core, dialect="excel", fieldnames=HEADERS)
                blank.writeheader()
                for line in temp:
                    tmp = deepcopy(line)
                    tmp.pop("out")
                    blank.writerow(tmp)
            return temp

        return wrapper

    return dump


@json_converter(OUT)
@to_csv(FILENAME)
@repeat(REPETITIONS)
@wr_roots
def worker(*args):
    less_m = abs(args[0]) if args[0] else 100
    while True:
        yield {
            HEADERS[0]: randint(0, less_m),
            HEADERS[1]: randint(0, less_m),
            HEADERS[2]: randint(0, less_m)
        }


if __name__ == '__main__':
    worker()
