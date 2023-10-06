"""
Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:

Инициализация матрицы. Конструктор класса должен принимать
 количество строк rows и
 количество столбцов cols и
 создавать матрицу с нулевыми значениями.

Операция сложения матриц. Реализуйте метод __add__,
который позволяет складывать две матрицы одинаковых размеров.

Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными размерами (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).

Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.

Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы, где элементы строки разделены пробелами, а строки сами разделены символами новой строки.

Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__, который возвращает строку, которую можно использовать для создания нового объекта класса Matrix.
"""


class Matrix:
    def __init__(self, rows: int, cols: int, default_value: int = 0):
        self.default_value = default_value
        self.rows = rows
        self.cols = cols
        self.data = [[self.default_value] * cols for i in range(rows)]

    def __add__(self, other: 'Matrix'):
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError("only equally sized matrices")
        out = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                out.data[i][j] = self.data[i][j]+other.data[i][j]
        return out

    def __mul__(self, other: 'Matrix'):

        # if self.cols != other.cols or self.rows != other.rows:
        #     raise ValueError("only equally sized matrices")
        out = Matrix(self.rows, self.cols)
        for i in range(self.cols):
            for j in range(self.rows):
                out.data[i][j] = self.data[i][j] * other.data[i][j]
        return out

    def __eq__(self, other: 'Matrix'):

        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError("only equally sized matrices")
        for i in range(self.cols):
            for j in range(self.rows):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __str__(self):
        out = ""
        for i in range(self.rows):
            for j in range(self.cols):
                out = out+f"{self.data[i][j]} "
            out = out.strip()
            out += "\n"
        return out

    def __repr__(self):
        return f"Matrix({self.rows},{self.cols},{self.default_value})"
        return f"{self.__class__.__name__}: {self.rows=}, {self.cols=}, {self.default_value=}"


if __name__ == '__main__':
    # print()
    #     a = Matrix(4, 2)
    #     b = Matrix(2, 4)
    c = Matrix(3, 2)
    c.body = [[1,2],[3,4],[5,6]]
    print(c)
    cd = c
    print(cd+c)
    #     for i in a, b, c:
    #         print()
    #         print(*i.data, sep="\n")
    # a = Matrix(2, 2, 1)
    # b = Matrix(2, 2, 3)
    # c = a+b
    # print(*c.data, sep="\n")
    # d = (Matrix(5, 5))
    # try:
    #     print(d+c)
    # except ValueError as e:
    #     print(e.args[0])
    # a = Matrix(3, 3, 2)
    # print(a)
    # print(f"{a=}")
    # b = Matrix(3, 3, 4)
    # c = a * b
    # print(*c.data, sep="\n")
    # assert a * b == c
    # assert a != b
