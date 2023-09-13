"""
Создайте модуль с функцией внутри. # файл
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import choice


def quess_game(bot: int, top: int, *, guesses: int):
    answer = choice(range(bot, top))
    print(f"#debug:{answer}")
    while guesses:
        tmp = int(input(f"Угадай число между {bot} и {top}?"))
        if tmp == answer:
            return True
        guesses -= 1
        print("больше" if tmp < answer else "меньше", '.', guesses, "попыток осталось")
    return False


if __name__ == '__main__':
    print(quess_game(1, 10, guesses=3))
