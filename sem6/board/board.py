"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
 Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так,
 чтобы они не били друг друга.
 Вам дана расстановка 8 ферзей на доске, определите,
 есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел,
 каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину,
 а если бьют - ложь.
"""
from copy import deepcopy


def init_field(size: int = 8) -> list[list[int]]:
    """
    пересоздаём доску
    :return:
    """
    out = []
    buffer = [0] * size
    for i in range(size):
        out.append(deepcopy(buffer))
    return out


def put_queen(desk: list[list[int]], pos: tuple[int, int] = None):
    desk[pos[0]][pos[1]] = 1


def __pos_valid(desk: list[list[int]], pos: tuple[int, int]) -> bool:
    limit = 1

    # 9-3
    if sum(desk[pos[0]]) > limit:
        return False
    # 12-6
    temp = 0
    for i in range(0, len(desk)):
        temp += desk[pos[1]][i]
        if temp > limit:
            return False
    # 1-8
    temp = 0
    j, k = pos
    while True:
        try:
            temp += desk[j][k]
            j -= 1
            if j < 0:
                break
            k -= 1
            if k < 0:
                break
            if temp > limit:
                return False
        except IndexError:
            break  # expected behavior
    j, k = pos
    while True:
        try:
            j += 1
            k += 1
            temp += desk[j][k]
            if temp > limit:
                return False
        except IndexError:
            break  # expected behavior
    # 11-4
    temp = 0
    j, k = pos
    while True:
        try:
            temp += desk[j][k]
            j += 1
            if j < 0:
                break
            k -= 1
            if k < 0:
                break
            if temp > limit:
                return False
        except IndexError:
            break
    j, k = pos
    while True:
        try:
            j -= 1
            if j < 0:
                break
            k += 1
            temp += desk[j][k]

            if temp > limit:
                return False
        except IndexError:
            break
    return True


def rigged_case(*positions: tuple[int, int]) -> bool:
    """
    тестируем вариант доски
    """
    test = init_field()
    for i in positions:
        put_queen(test, i)
    for i in positions:
        if not __pos_valid(test, i):
            return False
    return True

    pass


if __name__ == '__main__':
    print(rigged_case((0, 0), (1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2)))
    print(rigged_case((0, 0), (1, 1)))
