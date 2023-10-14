"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class PositiveInts:
    def __init__(self, min_value: int = 1):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(self, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("int required")
        if value < self.min_value:
            raise ValueError(f"must exceed {self.min_value}")
        self._value = value

    def __str__(self):
        return str(self._value)


class RectangleWithDescriptors:
    w = PositiveInts(1)
    h = PositiveInts(1)

    def __init__(self, w, h):
        self._w = w
        self._h = h

    def __str__(self):
        return f"Rectangle {self.w}x{self.h}"

    def per(self):
        return 2 * (self.h + self.w)

    def sq(self):
        return self.h * self.w

    def __eq__(self, other: 'RectangleWithDescriptors'):
        return self.h == other.h and self.w == other.w


if __name__ == '__main__':
    for i in ((0, 0), (0, 1), (1, 1)):
        try:
            print(f"{RectangleWithDescriptors(i[0], i[1])}")
        except (TypeError, ValueError) as e:
            print(e)
