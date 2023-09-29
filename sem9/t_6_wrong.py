"""
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
from functools import wraps
from pathlib import Path
from typing import Callable
from t_5 import json_arg, repeat_n_times, validate_input, randomized

FILENAME_U = Path("t6_out.json")


def json_arg_u(name: Path):
    return json_arg(name)


def repeat_n_times_u(n: int):
    return repeat_n_times(n)


def validate_input_n(func: Callable):
    return validate_input(func)


@repeat_n_times_u(n=3)
@json_arg_u(name=FILENAME_U)
@validate_input_n
def randomized_u(attempts: int, secret: int):
    return randomized(attempts, secret)


json_arg.__doc__ = "Переводим в json"
repeat_n_times.__doc__ = "Повторяем n раз"
validate_input.__doc__ = "Отсеиваем чушь"
randomized.__doc__ = "Угадываем число"

if __name__ == '__main__':
    randomized_u(3, 999)
