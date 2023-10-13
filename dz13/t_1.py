"""
Добавьте в задачу Rectangle, которую писали ранее,
 исключение NegativeValueError, которое выбрасывается при некорректных значениях
  ширины и высоты, как при создании объекта, так и при установке их через сеттеры.
"""

from dz11.t3 import Rectangle
from t_1_ex import NegativeValueError


class RectanglePositive(Rectangle):
    limit = 0

    def __init__(self, width: int, height: int):
        self._height = width
        self._width = width
        if width <= self.limit:
            raise NegativeValueError("width", width)
        if height <= self.limit:
            raise NegativeValueError("height", height)
        super().__init__(width, height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new: int):
        if new <= self.limit:
            raise NegativeValueError("width", new)
        self._width = new

    @height.setter
    def height(self, new: int):
        if new <= self.limit:
            raise NegativeValueError("height", new)
        self._height = new


if __name__ == '__main__':
    try:
        RectanglePositive(-2, 2),
    except NegativeValueError as e:
        print(e)
    a = RectanglePositive(3, 5)
    a.width = 4
    a.height = 5
    print(a)
    try:
        a.width = -1
    except NegativeValueError as e:
        print(e)
    try:
        a.height = -1
    except NegativeValueError as e:
        print(e)
    print(a)
