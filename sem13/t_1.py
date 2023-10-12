"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def while_True():
    while True:
        tmp = input("dai 4islo plz")
        try:
            return int(tmp)
        except ValueError:
            pass
        try:
            return float(tmp)
        except ValueError:
            print("e6e raz poprobyi")


if __name__ == '__main__':
    print(while_True())
