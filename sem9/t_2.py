"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку
 числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

from typing import Callable
from random import choice


def get_arguments(func: Callable):
    print()
    def validate(*args, **kwargs):
        hc_attempts = range(1, 11)
        hc_secret = range(1, 101)
        atts_ = args[0] if args[0] in hc_attempts else choice(hc_attempts)
        secret_ = args[1] if args[1] in hc_secret else choice(hc_secret)
        print(f"debug:{atts_=},{secret_=}")
        return func(atts_, secret_)

    return validate


@get_arguments
def randomized(attempts: int, secret: int) -> bool:
    while attempts:
        print(f"{attempts=}")
        if int(input("guess?")) == secret:
            return True
        attempts -= 1
    return False


if __name__ == '__main__':
    print(f"{randomized(5   ,5)=}")
