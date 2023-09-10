"""
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def gfib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a, b


inf = iter(gfib())

while True:
    print(print(next(inf)))
    if input("q?").lower() == "q":
        break
