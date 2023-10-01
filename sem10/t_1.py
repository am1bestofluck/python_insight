"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from math import pi


class Circle:
    def __int__(self, r: int):
        self._r = r

    def per(self):
        return 2 * pi * self._r

    def sq(self):
        return pi * pow(self._r, 2)
