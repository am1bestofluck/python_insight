"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств
"""

from sem11.t_5 import RectangleExtended


class RectanglePositiveSidesOnly(RectangleExtended):
    positive_limit = 1  # проверяем размеры на положительность

    def __init__(self, *args):
        self.width = args[0]  # спорно!
        self.height = args[1]
        super().__init__(*args)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, val: int):
        if val < self.positive_limit:
            raise AttributeError("expected positive width")

        self._width = val

    @height.setter
    def height(self, val):
        if val < self.positive_limit:
            raise AttributeError("expected positive height")
        self._height = val


if __name__ == '__main__':
    for i in (
            (1, 0),
            (-3, 1),
            (1, 1)
    ):
        try:
            a = RectanglePositiveSidesOnly(i[0], i[1])
            print("ok", i)
        except AttributeError:
            print("fail with ", i)
