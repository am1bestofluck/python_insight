"""
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""

from sem12_m.t_4 import RectanglePositiveSidesOnly


class RectangleMemoryTweak(RectanglePositiveSidesOnly):
    __slots__ = ("w", "h")

    def __init__(self, *args):
        super().__init__(*args)


class DumbBell:
    __slots__ = ("_weight",)

    def __init__(self, weight):
        self._weight = weight


if __name__ == '__main__':
    try:
        a = RectangleMemoryTweak(3, 5)
        print(a.__dict__)
        print(a.__slots__)
        a.w = True
        a.z = AssertionError
        print(a.__dict__)
        print(" c наследованием не проканало, и вообще странно.",
              "Получается что то что есть в слотс не попадает в dict")
    except BaseException as e:
        print("не выстрелит...")

    try:
        b = DumbBell(3)
        b.noway = 1
    except AttributeError:
        print("works as expected")
