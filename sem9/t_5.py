"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
from random import choice
from typing import Callable


def to_json(func: Callable):
    def wrapper(*args, **kwargs):
        print(args)
        return True

    return wrapper


def repeat_n_times(n: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal n
            out = {}
            for i in range(n):
                temp = func(args[0],args[1])
                out[str((temp[0],temp[1]))] = temp[2]
            return out

        return wrapper

    return deco


def validate_input(func: Callable):
    hc_attempts = range(1, 11)
    hc_secret = range(1, 101)

    def deco(*args, **kwargs):
        nonlocal  hc_secret,hc_attempts
        a = args[0] if args[0] in hc_attempts else choice(hc_attempts)
        b = args[1] if args[1] in hc_secret else choice(hc_secret)
        print(f"debug:{a=},{b=}")
        return a, b, func(a, b)
    return deco


@repeat_n_times(3)
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
