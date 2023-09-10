"""
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.

"""
def long_():
    out = []
    for i in range(1,101):
        if not i%3 and not i%5:
            out.append("FizzBuzz")
            continue
        elif not i%3:
            out.append("Fizz")
            continue
        elif not i%5:
            out.append("buzz")
            continue
        else:
            out.append(i)
    print(out)

long_()
def short_():
    return list((i if not i%3 and not i%5 else ("fizz" if i%3 else "buzz")) for i in range(1,101))

short_()