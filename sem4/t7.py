"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


"""
from pprint import pp
from random import choices,sample
from string import ascii_lowercase
def main(descr:dict[str,list[int]]) -> bool:
    out = None
    temp = dict()
    for i in descr:
        temp[i] = sum(descr[i])
        print(f"{i}:{temp[i]}")
    for i in temp:
        if temp[i] <0:
            return False
    return  True

if __name__ == '__main__':
    inc = dict()
    for name_c in sample(ascii_lowercase,5):
        inc[name_c] = choices(range(-1_000_000,1_000_000,1000),k=4)
    pp(inc)
    print(main(inc))