"""
 Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.

"""
from random import choice

MAX = 10 ** 3


def main(str_i: str):
    out = dict()
    for eggs in str_i.strip().split():
        out[eggs] = chr(int(eggs))
    print(out)


if __name__ == '__main__':
    main(f"{choice(range(MAX))} {choice(range(MAX))}")
