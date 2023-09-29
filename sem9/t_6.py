"""
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
from pathlib import Path
from typing import Callable
from t_5 import json_arg, repeat_n_times, validate_input, randomized

FILENAME = Path("t6_out.json")

json_arg.__doc__ = "Переводим в json"
repeat_n_times.__doc__ = "Повторяем n раз"
validate_input.__doc__ = "Отсеиваем чушь"
randomized.__doc__ = "Угадываем число"


def json_arg_u(name: Path):
    json_arg(name)


def repeat_n_times_u(n: int):
    repeat_n_times(n)


def validate_input_n(func: Callable):
    validate_input(func)


def randomized_u(attempts: int, secret: int):
    randomized(attempts, secret)
