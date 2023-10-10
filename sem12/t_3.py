"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.

"""
from sem12.t_1 import FactorialOf


class FactorialIterator:
    def __init__(self, stop_i: int, start_i=1, step: int = 1):
        self._st = start_i
        self._end = stop_i
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self._st < self._end:
            self._st += self._step
            return FactorialOf(self._st).out
        raise StopIteration


if __name__ == '__main__':
    a = iter(FactorialIterator(10))
    for item in a:
        print(item)
