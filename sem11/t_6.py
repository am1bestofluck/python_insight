"""
Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения

"""
from sem11.t_5 import RectangleExtended, Rectangle


class RectangleExtendedWithSquares(RectangleExtended):
    def __init__(self, *args):
        super().__init__(*args)

    def __eq__(self, other: Rectangle):
        return self.sq() == other.sq()

    def __gt__(self, other):
        return self.sq() > other.sq()

    def __ge__(self, other):
        return self == other or self > other


if __name__ == '__main__':
    a = RectangleExtendedWithSquares(1, 1)
    b = RectangleExtendedWithSquares(2, 2)
    c = RectangleExtendedWithSquares(3, 3)
    d = RectangleExtendedWithSquares(1, 1)
    assert a + b == c
    assert c - b == a
    assert d == a
    assert c > b > a
    assert a <= b <= c
