"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.__age = kwargs['age']
        self.hobby = kwargs['hobby']

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def get_full_name(self):
        return self.name
