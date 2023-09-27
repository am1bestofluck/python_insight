"""
Создайте декоратор с параметром.        +
Параметр - целое число, количество запусков декорируемой
функции.                                +

"""
from random import choice
from typing import Callable


def repeat_n_times(n: int):
    def deco(func:Callable):
        def wrapper(*args, **kwargs):
            nonlocal n
            out = []
            for i in range(n):
                out.append(func())
            return out
        return wrapper
    return  deco

@repeat_n_times(n =10)
def flip_coin():
    return choice([True, False])

if __name__ == '__main__':
    print(flip_coin())