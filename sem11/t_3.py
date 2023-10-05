"""
Задание №3
Добавьте к задачам 1 и 2 строки документации для классов.
"""

from sem11.t_2 import Archive
from sem11.t_1 import MyString

MyString.__init__.__doc__ = "qwe"  # странно, а здесь перезаписывается
MyString.__doc__ = "Строчка с цифровой подписью"


class ArchiveUpd(Archive):
    """Приношу глубочайшие соболезнования тому кто оформлял задание №2"""

    def __init__(self, a: str, b: int):
        """Наследуем от родителя"""
        super().__init__(a, b)

    @classmethod
    def get_protected(cls):
        """Хахаха, ловим баги релизной версии на семинарах. Как мило!
        # https://delimitry.blogspot.com/2014/08/python-docstrings.html :("""
        return super().get_protected()


if __name__ == '__main__':
    try:
        Archive.get_protected.__doc__ = "asd"
    except AttributeError:
        pass
        print("""'Почему ты сделал ещё один класс?' Да вот почему.
        Редактировать исходник - неок, а перезаписать докстринг метода - на 3.11 нельзя
        Впрочем какое твоё дело.
        UPD: в 3.13 уже можно :)""")
    print(help(ArchiveUpd))
    print("\n*" * 3)
    print(help(MyString))
