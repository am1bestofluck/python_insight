"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""


# рузкий на отличьна

class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str, price: int):
        print("init")
        self.names = [name]
        self.prices = [price]


a = Archive("lobsters", 3)
print(a.__dict__)
b = Archive("fish",5)
print(b.__dict__)

b = Archive()
print(a == b)
