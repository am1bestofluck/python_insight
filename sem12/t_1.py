"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

"""


class FactorialOf:
    _values = {}

    def __init__(self, base: int):
        self._base = base
        self._calc()

    def _calc(self):
        self.out = 1
        for i in range(1, self._base + 1):
            if i not in FactorialOf._values:
                print("calc of", i)
                self.out = self.out * i
                FactorialOf._values[i] = self.out
            else:
                self.out = FactorialOf._values[i]

    def __call__(self):
        return self.out

    def get_vals(self):
        return FactorialOf._values


if __name__ == '__main__':
    a = FactorialOf(100)
    print(a())
    b = FactorialOf(99)
    print(b())
    print(b.get_vals())
