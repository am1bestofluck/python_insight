"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
from random import choices,sample
def main(list_i:list[int],*,i_l:int,i_u:int):
    borders= range(len(list_i))
    lower_limit = i_l if i_l in borders  else 0
    upper_limit = i_u if i_u in borders else len(list_i)
    return sum(list_i[lower_limit:upper_limit])

if __name__ == '__main__':
    sample_=choices(range(100),k=10)
    pos= sample(range(10),k=2)
    out = main(sample_,i_l=min(pos),i_u=max(pos))
    print(sample_)
    print(pos)
    print(out)