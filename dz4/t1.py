"""
Напишите функцию для транспонирования матрицы
"""

from random import sample, choice
from pprint import pp


class Matrix:
    MAX_WIDTH = 20
    MAX_HEIGHT = 20
    MAX_UNIT = 100
    __shortname = "Матрица"

    def __init__(self, height=None, width=None):
        self.__width = width if width else choice(range(1, Matrix.MAX_WIDTH))
        self.__height = height if height else choice(range(1, Matrix.MAX_HEIGHT))
        self.__field = self.rebuild_matrix()

    def rebuild_matrix(self):
        base = []
        for i in range(self.__height):
            base.append(sample(range(Matrix.MAX_UNIT), k=self.__width))
        return base

    def get(self, state: str = "default") -> list[list[int]]:
        print(state)
        return self.__field

    def __str__(self):
        return f"{Matrix.__shortname}, размерностью {self.__width}*{self.__height}."

    def __repr__(self):
        return f"{self.__class__.__name__}[{self.__width}:{self.__height}]"

    def rotate(self, *directions: bool):
        for i in directions:
            hint = "rotated cw" if bool(i) else "rotated ccw"
            self.__rotate(clock_wise=i)
            pp(self.get(hint))

    def __rotate(self, *, clock_wise: bool):
        temp = [[None] * self.__height] * self.__width
        walk = range(self.__height-1, -1, -1) if clock_wise else range(self.__height)
        for w in range(self.__width):
            buffer = []
            for h in walk:
                buffer.append(self.__field[h][w])
            floor = w if clock_wise else self.__width-w-1
            temp[floor] = buffer
        self.__field = temp
        self.__width, self.__height = self.__height, self.__width

    def __counter_clock_wise(self):
        pass


def main():
    a = Matrix()
    pp(a)
    pp(a.get())
    a.rotate(1, 0)  # , 1, 0, 0)


if __name__ == '__main__':
    main()
