
"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.

"""

txt = input("line?")
d_letters = {ord(i) for i in txt}

it = iter(d_letters)

for i in range(5):
    print(next(it))