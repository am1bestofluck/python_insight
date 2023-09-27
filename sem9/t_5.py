"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
from typing import Callable


def to_json(func: Callable):
    def wrapper(*args, **kwargs):
        print(args)
        return True

    return wrapper


def validate_input(func: Callable):
    def wrapper(*args, **kwargs):
        return func(args[0], args[1])

    return wrapper

@to_json
@validate_input
def randomized(attempts: int, secret: int) -> bool:
    while attempts:
        print(f"{attempts=}")
        if int(input("guess?")) == secret:
            return True
        attempts -= 1
    return False


if __name__ == '__main__':
    randomized(3, 5, randomized.__name__)
