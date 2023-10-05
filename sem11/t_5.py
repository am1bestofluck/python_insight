"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""

from sem10.t_2 import Rectangle


class RectangleExtended(Rectangle):
    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other: Rectangle):
        tmp = (self.per() + other.per()) / 4
        return RectangleExtended(tmp, tmp)

    def __sub__(self, other):
        temp = super().per() - other.per() if super().per() - other.per() > 0 else None
        if temp is not None:
            tmp = (self.per() - other.per()) / 4
            return RectangleExtended(tmp, tmp)
        return temp

    def __str__(self):
        return f"Rectangle {self.w}*{self.h}"


if __name__ == '__main__':
    a = RectangleExtended(3, 4)
    b = RectangleExtended(3, 4)
    print(str(a + b))
    print(str(a - b))
