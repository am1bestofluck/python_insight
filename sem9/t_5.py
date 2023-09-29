"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
import json
from pathlib import Path
from random import choice
from typing import Callable

FILENAME = Path("t5_out.json")


def json_arg(name: Path):
    def to_json(func: Callable, **kwargs):
        print("dump")

        def json_wrapper(*args, **kwargs):
            nonlocal name
            if not name.exists():
                content = {}
            else:
                with open(name, encoding="utf-8", mode="rt") as b4:
                    try:
                        content: dict = json.loads(b4.read())
                    except json.JSONDecodeError:
                        content = dict()

            res = func(*args)
            content.update(res)

            with open(name, encoding="utf-8", mode="wt") as after:
                json.dump(obj=content, fp=after, indent=1)
            return res

        return json_wrapper

    return to_json


def repeat_n_times(n: int):
    print("repeat")

    def repeat_deco(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal n
            out = {}
            for i in range(n):
                func(args[0], args[1])

            return

        return wrapper

    return repeat_deco


def validate_input(func: Callable):
    print("validate")
    hc_attempts = range(1, 11)
    hc_secret = range(1, 101)

    def deco(*args, **kwargs):
        nonlocal hc_secret, hc_attempts
        a = args[0] if args[0] in hc_attempts else choice(hc_attempts)
        b = args[1] if args[1] in hc_secret else choice(hc_secret)
        print(f"debug:{a=},{b=}")
        return {f"{a},{b}": func(a, b)}

    return deco


@repeat_n_times(1)
@json_arg(FILENAME)
@validate_input
def randomized(attempts: int, secret: int) -> bool:
    print('!')
    while attempts:
        print(f"{attempts=}")
        if int(input("guess?")) == secret:
            return True
        attempts -= 1
    return False


if __name__ == '__main__':
    print(randomized(3, 500))
