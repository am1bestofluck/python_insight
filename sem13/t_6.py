"""
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта.
"""
from sem13.t_3 import LevelException


class LevelExceptionExtended(LevelException):
    def __init__(self, has: int, needs: int):
        self.has = has
        self.needs = needs

    def __str__(self):
        return f"Cant create user with permission level '{self.needs}' on  access  level '{self.has}'."


if __name__ == '__main__':
    print("Было плюс минус готово  на этапе создания класса, ну да ладно ")
    raise LevelExceptionExtended(3, 2)
