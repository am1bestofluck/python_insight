"""
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
"""
def main():
    lst = []
    for i in range(10):
        lst.extend((i,i))
    lst_short = list(set(lst))
    lst_long =[]
    for i in lst:
        if i in lst_long:
            continue
        lst_long.append(i)
    print(lst)
    print(lst,lst_short,lst_long)
