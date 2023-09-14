"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

from random import choices, choice
from winsound import Beep
from board import init_field, put_queen, __pos_valid, rigged_case
from datetime import  datetime

INIT = datetime.now()
def new_set() -> list[tuple[int, int]]:

    out = []
    a = init_field()
    first_queen = choices(range(len(a)), k=2)
    put_queen(a, first_queen)
    while len(out) != 8:
        picks = []
        for i in range(len(a)):
            for j in range(len(a)):
                if __pos_valid(a, (i, j)) and not a[i][j]:
                    picks.append((i, j))
        try:
            current_queen = choice(picks)
        except IndexError:
            out = []
            a = init_field()
            first_queen = choices(range(len(a)), k=2)
            put_queen(a, first_queen)
            continue
        put_queen(a, current_queen)
        out.append(current_queen)
    return out

def new_set_alt() -> list[tuple[int,int]]:
    out = []
    a = init_field()
    first_queen = choices(range(len(a)), k=2)
    put_queen(a, first_queen)

    while len(out)!=8:
        place = choices(range(len(a)),k=2)
        if __pos_valid(a,place) and not a[place[0]][place[1]]:
            put_queen(a,place)
            out.append(place)
    return out

def main():
    cases = 4
    while cases:
        deck = new_set_alt()
        a = rigged_case(*deck)
        if a:
            print(INIT - datetime.now())
            cases -= 1


if __name__ == '__main__':
    main()
