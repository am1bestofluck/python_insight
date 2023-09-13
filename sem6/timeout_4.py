"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами
 отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана
 загадка или ноль, если попытки исчерпаны.

"""


def riddle(*, riddle_: str, answer: int, guesses: int, variants: list[str]):
    print(riddle_)
    print(f"варианты ответа:{chr(10)}{list(enumerate(variants))}")
    while guesses:
        if int(input("вариант ответа?")) == answer:
            return guesses
        guesses -= 1
    return guesses


if __name__ == '__main__':
    print(
        riddle(riddle_="Море Я без воды, дорога без пыли, горы без ветра. Что Я?",
               guesses=3,
               answer=1,
               variants=["трепло", "карта", "поциент", "мавродик", "None", "продам гараж"]
               )
    )
