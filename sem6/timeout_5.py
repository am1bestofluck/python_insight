"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

"""

from . import timeout_4


# riddle_: str, answer: int, guesses: int, variants: list[str]
def riddles_dict() -> dict[str:list[str | int]]:
    return {
        "1+1": [0, 3, ['2', '3', '4', '5', '6']],
        "1+2": [1, 3, ['2', '3', '4', '5', '6']],
        "2+2": [2, 3, ['2', '3', '4', '5', '6']],
        "2+3": [3, 3, ['2', '3', '4', '5', '6']]
    }


def main():
    w = riddles_dict()
    for riddle_ in w:
        print(timeout_4.riddle(riddle_=riddle_,
                     guesses=w[riddle_][1],
                     answer=w[riddle_][0],
                     variants=w[riddle_][2]))


if __name__ == '__main__':
    main()
