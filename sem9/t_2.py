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


def outer_decor(func_in: Callable):
    print("outer decor")
    attempts = range(1, 11)
    secrets = range(1, 101)

    def inner_decor(*args, **kwargs):
        nonlocal attempts, secrets
        guesses = args[0] if args[0] in attempts else choice(attempts)
        secret = args[1] if args[1] in secrets else choice(secrets)
        result = func_in(guesses, secret)
        return result

    return inner_decor


@outer_decor
def guess_game(guesses: int, secret: int):
    print(locals())


if __name__ == '__main__':
    guess_game()
