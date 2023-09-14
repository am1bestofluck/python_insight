"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

from random import choices, choice

from board import init_field, put_queen, __pos_valid, rigged_case


def new_set() -> list[tuple[int, int]]:
    out = []
    a = init_field()
    first_queen = choices(range(len(a)), k=2)
    put_queen(a, first_queen)
    while len(out) != 8:
        picks = []
        for i in range(len(a)):
            for j in range(len(a)):
                if __pos_valid(a, (i, j)):
                    picks.append((i, j))
        try:
            current_queen = choice(picks)
        except IndexError:
            break
        put_queen(a, current_queen)
        out.append(current_queen)
    return out


def main():
    cases = 4
    while cases:
        deck = new_set()
        if len(deck) != 8:
            print(len(deck))
        a = rigged_case(*deck)
        if a:
            cases -= 1
            print(f"{cases=}")


if __name__ == '__main__':
    main()
