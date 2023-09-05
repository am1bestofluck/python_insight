"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
from random import sample


def bubble_sort(l: list):
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]: # 8 4 *// 8 4 4 //
            l[i],l[i+1] = l[i+1],l[i]
            i = 0
        else:
            i += 1

    return l


def main():
    a = sample(range(100), 10)
    print(a)
    b = bubble_sort(a)
    print(b)
    assert set(a) == set(b)


if __name__ == '__main__':
    main()
