"""
Дан список повторяющихся элементов.+
Вернуть список с дублирующимися элементами.+
В результирующем списке не должно быть дубликатов.+
"""

from random import choices

LIST_SIZE = 30


def get_noise(list_i) -> list:
    return [i for i in set(list_i) if list_i.count(i) > 1]


def main():
    global LIST_SIZE
    for _ in range(3):
        temp_ = sorted(choices(range(LIST_SIZE // 2), k=LIST_SIZE))
        print(f"{temp_=}")
        out = sorted(get_noise(temp_))
        print(f"{out=}")


def testable(ints: list[int]):
    return sorted(get_noise(ints))


if __name__ == '__main__':
    main()
