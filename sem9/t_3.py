"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает.                                                 +
 При повторном вызове файл должен
расширяться, а не перезаписываться.                         +
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.                                               +
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.        +
Имя файла должно совпадать с именем декорируемой            +
функции.

"""
import json
from pathlib import Path
from typing import Callable

try:
    from t_2 import randomized
except ImportError:
    from .t_2 import randomized




def to_json(func: Callable):
    OUT = Path(f"{func.__name__}.json")
    def wrapper(*args, **kwargs):
        nonlocal  OUT
        print(args)
        out = func(args[0], args[1])

        print(f"{args} = {out}")
        try:
            with open(file=OUT, mode="rt+", encoding="utf-8") as output_j:
                before = json.loads(output_j.read())
        except (FileNotFoundError,json.JSONDecodeError):
            before ={}
        with open(file=OUT, mode="wt", encoding="utf-8") as output_j:
            before.update({str(args): out})
            before.update(kwargs)
            output_j.write(json.dumps(before,indent=1))
        return out

    return wrapper


@to_json
def what_is_dry(a: int, b: int,**kwargs):
    return randomized(a, b)


if __name__ == '__main__':
    a, b = int(input("attempts?")), int(input("secret?"))
    what_is_dry(a, b,this_may_be_fun=True,is_it=False)
