"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.

"""

from typing import Callable


def count_guesses(guesses: int = 10) -> [Callable, bool]:
    """угадываем secret за guesses попыток"""
    guesses_m = 0

    def randomized(secret: int) -> bool:
        nonlocal guesses, guesses_m

        while guesses:
            print(f"{guesses=}")
            if int(input("guess?")) == secret:

                print(f'угадали за  {guesses_m+1}!')
                return True
            guesses_m += 1
            guesses -= 1
        print(f'не угадали!')
        return False

    return randomized


if __name__ == '__main__':
    print(count_guesses(int(input("guesses?")))(int(input("secret?"))))
