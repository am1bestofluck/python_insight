"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class UserException(Exception):
    pass


class LevelException(UserException):
    def __init__(self, note: str):
        self.note = note

    def __str__(self):
        return f"Здесь вам не тут: {self.note}"


class AccessException(UserException):
    def __init__(self, note: str):
        self.note = note

    def __str__(self):
        return f"Ты кто?: {self.note}"


if __name__ == '__main__':
    try:
        raise LevelException("oops")
    except LevelException:
        raise AccessException("no way")
    finally:
        print("it's ok")

