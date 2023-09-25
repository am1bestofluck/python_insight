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


def count_guesses(func) -> [Callable, bool]:
    def wrapper(*args):
        guesses_hc = range(1, 11)
        secret_hc = range(1, 111)

        if args[0] not in guesses_hc:
            guesses = choice(guesses_hc)
        else:
            guesses = args[0]
        if args[1] not in secret_hc:
            secret = choice(secret_hc)
        else:
            secret = args[1]
        return func(guesses, secret)

    return wrapper


@count_guesses
def randomized(guesses, secret) -> bool:
    while guesses:
        print(f"{guesses=}")
        if int(input("guess?")) == secret:
            return True

        guesses -= 1
    print(f'не угадали!')
    return False


if __name__ == '__main__':
    print(randomized(1, 7))
