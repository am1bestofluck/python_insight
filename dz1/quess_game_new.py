from random import choice
from string import digits


class HangmanNumbersGame(object):
    """
        Запускаем игру вызовом roll()
    """
    __limit_lower = 0
    __limit_upper = 1000
    __guesses_default = 10

    def __new__(cls):
        # честно украдено с https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
        if not hasattr(cls, 'instance'):
            cls.instance = super(HangmanNumbersGame, cls).__new__(cls)
        return cls.instance

    def roll(self) -> bool:

        """roll возвращает True если получилось угадать
        guesses- количество оставшихся попыток
        out - выводное значение, обрывает цикл если мы угадали раньше 10-и попыток
        limit_lower, limit_upper  - границы выборки
        """
        win = {"Me": "I keep the cookie", "Script": "Script steals the cookie"}
        guesses = self.__guesses_default
        turn = input("Who guesses now? Digit for Myself, else for script")
        out = False
        limit_lower = self.__limit_lower
        limit_upper = self.__limit_upper
        if set(turn).issubset(set(digits)):
            goal = self.__input_int(prompt="Which number do I guess?", inherited=turn)
            while guesses:
                guess = self.__ask(limit_lower, limit_upper)
                guesses -= 1
                print(f"Script guessed {guess}. {guesses} attempts remain.")
                if guess > goal:
                    limit_upper = guess
                elif guess < goal:
                    limit_lower = guess
                else:
                    print(win["Script"])
                    out = True
                    return out
            print(win["Me"])
            return out
        else:
            goal = choice(range(limit_lower, limit_upper))
            print("hint! script guessed", goal)
            while guesses:
                guess = self.__input_int(prompt=f"guess between {limit_lower} and {limit_upper}",
                                         limit_lower_i=limit_lower, limit_upper_i=limit_upper)
                guesses -= 1
                print(f"I guessed {guess}. {guesses} attempts remain.")
                if guess > goal:
                    print("Too much.")
                    limit_upper = guess
                elif guess < goal:
                    print("Too few.")
                    limit_lower = guess
                else:
                    print(win["Me"])
                    out = True
                    return out
            print(win["Script"])
            return out

    def __ask(self, limit_lower: int, limit_upper: int) -> bool:
        return choice(range(limit_lower, limit_upper))

    def __input_int(self, prompt: str, inherited: str = None, limit_upper_i: int = None, limit_lower_i: int = None) -> int:
        limit_upper_m = limit_upper_i if limit_upper_i else self.__limit_upper
        limit_lower_m = limit_lower_i if limit_lower_i else self.__limit_lower
        while True:
            try:
                if inherited is not None:
                    buffer = int(inherited)
                    inherited = None
                else:
                    buffer = int(input(prompt))
                if buffer not in range(
                        limit_lower_m,
                        limit_upper_m):
                    print(f"Must correspond [{limit_lower_m}" \
                          +f"..{limit_upper_m})")
                    continue
                return buffer
            except TypeError:
                print("not a number")
                continue


def main():
    a = HangmanNumbersGame()
    print(id(a))
    b = HangmanNumbersGame()
    print(id(b))
    a.roll()


if __name__ == "__main__":
    main()
