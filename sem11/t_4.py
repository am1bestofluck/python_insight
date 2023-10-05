"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""
from sem11.t_3 import ArchiveUpd


class ArchiveRepresented(ArchiveUpd):
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b
        super().__init__(self.a, self.b)

    def __str__(self):
        return f"Archive: {self.a}, {self.b}"

    def __repr__(self):
        return f"Archive with buffer: {super().get_protected()}"


if __name__ == '__main__':
    a = ArchiveRepresented("a", 3)
    a = ArchiveRepresented("b", 4)
    print(f"{a}")
    print(f"{a=}")
