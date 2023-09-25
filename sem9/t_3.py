"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.

"""
from json import loads, dump, load
from typing import Callable


def jsonize( func):
    def wrapper_j():

def get_args(func) -> [Callable, bool]:
    print("st")

    def wrapper(*args, **kwargs):
        list_args = [*args]
        list_kwargs = [*kwargs.values()]
        list_args.extend(list_kwargs)
        return func(list_args)

    print("ou")
    return wrapper


@get_args
def sum_ints(list_: list[int]):
    return sum(list_)


out = "t4_out.json"

if __name__ == '__main__':
    to_json = {}
    key = 1, 2, 4
    to_json[str(key)] = sum_ints(*key)
    with open(out, "r") as core:
        try:
            lines = core.readlines()
            tmp = "".join(lines)
            base = loads(tmp)
        except:
            base = {}
    base.update(to_json)
    with open(out, "w") as core:
        dump(base,core)
