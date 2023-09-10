"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def is_simple(n: int) -> bool:
    if n == 2:
        return True
    devisor = 2
    while n % devisor != 0:
        devisor += 1
    return devisor == n


def simple_(n):
    counter, iter_ = 0, 2
    while counter < n:
        if is_simple(iter_):
            counter += 1
            tmp =iter_
            iter_+=1
            yield tmp
        else:
            iter_ += 1


def maim():
    n = int(input("n?"))
    a = iter(simple_(n))
    m = n
    while m:
        print(next(a))
        m -= 1


if __name__ == '__main__':
    maim()
