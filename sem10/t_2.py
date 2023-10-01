"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __int__(self, *args):
        self.w = args[0]
        try:
            self.h = args[1]
        except IndexError:
            self.h = args[0]

    def per(self):
        return 2 * (self.h + self.w)

    def sq(self):
        return self.h * self.w
