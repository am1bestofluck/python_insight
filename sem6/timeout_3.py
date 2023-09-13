"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

"""

from random import choice
from sys import argv, exit
from . import timeout_2

def to_int():
    for arg in argv[1:]:
        yield int(arg)


def get_ints() -> []:
    args = []
    temp = iter(to_int())
    while True:
        try:
            args.append(next(temp))
        except StopIteration:
            return args
        except ValueError:
            exit(1)


def main():
    args = get_ints()
    if not args or len(args) > 3:
        exit(1)
    while len(args) != 3:
        try:
            args.append((choice(range(-args[1], args[1]))))
        except IndexError:
            args.append(choice(range(100)))

    print(timeout_2.quess_game(min(args[1:]), max(args[1:]), guesses=args[0]))


if __name__ == '__main__':
    main()
