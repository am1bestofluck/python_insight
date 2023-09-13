"""
Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать
 или ложь, если такая дата невозможна.
Для простоты договоримся,
что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года)
 действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
+
"""
from sys import argv
from datetime import datetime


def main():
    try:
        date_ = datetime.strptime(argv[1], "%d.%m.%Y")
        return True
    except ValueError:
        return False


def not_main():
    # date_ = list(map(int, sstr.split(".")))
    date_ = list(map(int, argv[1].split(".")))
    t = date_[2]
    years, months = range(1, 10000), range( 13)
    days = {
        2: 30 if not t % 400 or (t % 100 != 0 and t % 4 == 0) else 29,
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 1: 31
    }
    if date_[2] not in years:
        return False
    if date_[1] not in months:
        return False
    if date_[0] not in range(days[date_[1]]):
        return False
    return True


if __name__ == '__main__':
    print(not_main())
