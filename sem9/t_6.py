"""
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
from functools import wraps
import json
from pathlib import Path
from random import choice
from typing import Callable

FILENAME = Path("t6_out.json")


def json_arg(name: Path):
    """fail_json_arg"""
    def to_json(func: Callable, **kwargs):
        """fail_to_json"""
        @wraps(func)
        def json_wrapper(*args, **kwargs):
            """fail_json_wrapper"""
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
    def repeat_deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """fail"""
            nonlocal n
            out = {}
            for i in range(n):
                func(args[0], args[1])

            return

        return wrapper

    return repeat_deco


def validate_input(func: Callable):
    hc_attempts = range(1, 11)
    hc_secret = range(1, 101)

    @wraps(func)
    def deco(*args, **kwargs):
        """ok_v"""
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

    while attempts:
        print(f"{attempts=}")
        if int(input("guess?")) == secret:
            return True
        attempts -= 1
    return False


# err = "Fail"
randomized.__doc__ = """success"""
# validate_input.__doc__ = err
# json_arg.__doc__ = err
# repeat_n_times.__doc__ = err

if __name__ == '__main__':
    print(help(randomized))
