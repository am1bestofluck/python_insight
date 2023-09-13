"""
Добавьте в модуль с загадками функцию, которая принимает на вход
 строку (текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания
 из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

"""
from . import timeout_4
from . import timeout_5

__stats = dict()


def next_riddle():
    temp = timeout_5.riddles_dict()
    for i in temp:
        yield {i: timeout_4.riddle(riddle_=i, variants=temp[i][2],
                                   answer=temp[i][0], guesses=temp[i][1])}


def gather_stat():
    iter_ = iter(next_riddle())
    while True:
        try:
            __stats.update(next(iter_))
        except StopIteration:
            break




def full_game():
    gather_stat()
    print(f"{__stats=}")


if __name__ == '__main__':
    full_game()
