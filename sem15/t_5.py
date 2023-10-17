"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""

import argparse
from datetime import date, timedelta
import logging
from pathlib import Path
from typing import Callable

WEEK_DAYS = {
    "воскресенье": 6,
    "понедельник": 0,
    "вторник": 1,
    "среда": 2,
    "четверг": 3,
    "пятница": 4,
    "суббота": 5
}
MONTHS = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12}


def log_errors(path_file: Path):
    def log_inner(func: Callable):
        def wrapper(*args, **kwargs):
            nonlocal path_file
            logging.basicConfig(filename=path_file, filemode="at", encoding="utf-8", level=logging.INFO)
            out = None
            try:
                out = func(*args, **kwargs)
            except Exception as e:
                logging.error(f"{args[0]}: {e.args[0]}")
                return None
            logging.info(f"{args[0]} == {out}")
            return out

        return wrapper

    return log_inner


@log_errors(Path("t5_log.log"))
def parse_date(letters: str):
    """

    :param letters:
    :return: date
    # >>> parse_date("1-й четверг ноября")
    # datetime.date(2023, 11, 2)
    # >>> parse_date("4-я среда октябрЯ")
    # datetime.date(2023, 10, 25)
    """
    global WEEK_DAYS, MONTHS
    items = letters.split()
    if len(items) != 3:
        raise UserWarning(f"ожидаем 3 блока знаков разделённых пробелами, получили {len(items)}")
    try:
        try:
            index_ = int(items[0])
        except ValueError:  # в общем то ожидаемое поведение
            index_ = int(items[0].split("-")[0])
    except ValueError:
        raise ValueError("не смог прочитать номер дня")
    if index_ < 1:
        raise ValueError("порядковый номер для недели в месяце в множестве натуральных чисел")
    try:
        try:
            day_ = int(items[1])
        except ValueError:
            day_ = WEEK_DAYS[items[1].lower()]
    except KeyError:
        raise KeyError("не смог декодировать день недели")
    try:
        try:
            month_ = int(items[2])
        except ValueError:
            month_ = MONTHS[items[2].lower()]
    except KeyError:
        raise KeyError("не смог декодировать название месяца")
    if month_ not in range(1, 12 + 1):
        raise ValueError(f"не знаю месяц #{month_}")
    start = date(
        date.today().year,
        month_,
        1)  # ymd
    days_of_month_: dict[int, list[date]] = {}
    for i in WEEK_DAYS:
        days_of_month_[WEEK_DAYS[i]] = []
    while start.month == month_:
        days_of_month_[start.weekday()].append(start)
        start += timedelta(days=1)
    try:
        return days_of_month_[day_][index_ - 1]
    except IndexError:
        raise ValueError("Не получилось насчитать столько таких дней недели в этом месяце ")


def arg_parse() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('argdate', metavar='order_of weekday of_month', nargs=3)
    return " ".join(parser.parse_args().argdate)


if __name__ == '__main__':
    tests = arg_parse()
    parse_date(tests)
