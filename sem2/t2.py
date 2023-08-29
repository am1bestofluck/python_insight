"""
✔Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
 ✔Функции bin и oct используйте для проверки своего результата, а не для решения. Дополнительно:
 ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
 ✔Избегайте магических чисел
 ✔Добавьте аннотацию типов где это возможно
"""


def main():
    while True:
        try:
            n = int(input("gimme n"))
            break
        except ValueError:
            continue
    print("result_bin", bin(n))
    print("result_oct", oct(n))

    for base in [2, 8]:
        result = ""
        div = n
        while div > 0:
            div, mod = divmod(div, base)
            result = str(mod) + result
        print(base, result)


