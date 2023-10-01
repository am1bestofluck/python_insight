"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь

"""
from t_3 import Person


class Employee(Person):
    def __init__(self, **kwargs):
        self.code = kwargs['code']
        self.access = self.__calc_access()
        super().__init__()

    def __calc_access(self):
        return sum([int(i) for i in str(self.code)]) / 7
