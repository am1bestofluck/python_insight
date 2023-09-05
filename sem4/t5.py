"""
Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.

"""
from random import sample, choice
from string import ascii_lowercase
from pprint import pp


def main(table: list[list[str | int]]) -> dict[str, float]:
    out = dict()
    for line in table:
        out[line[0]] = line[1] * round(float(line[2][:-1]) * 0.01, 4)
    return out


if __name__ == '__main__':
    sample_ = zip(
        sample(ascii_lowercase, 5),
        sample(range(10000, 12000, 100), 5),
        [f"{choice(range(100))}.{choice(range(100))}%" for _ in range(5)])
    sample_ = list(sample_)
    print(sample_)
    print()
    print(main(sample_))
