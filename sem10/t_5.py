"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.birth_year = kwargs['birth_year']
        self.weight = kwargs['weight']

    def __repr__(self):
        raise NotImplementedError("только через наследников")


class Bird(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.food = kwargs['food']

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.name}, born in {self.birth_year}" \
               f", weights {self.weight} lb, eats {self.food}."


class Fish(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.water_type = kwargs['water_type']

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.name}, born in {self.birth_year}" \
               f", weights {self.weight} lb,lives in {self.water_type} water."


class Cat(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fur = kwargs['fur']

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.name}, born in {self.birth_year}" \
               f", weights {self.weight} lb, has {self.fur} fur"

def main():
    print(
        Bird(name="Boris", birth_year="2000", weight=5, food="fish"),
        Fish(birth_year="2003", weight=3, water_type="salty", name="Nemo"),
        Cat(birth_year=2006,weight=4,name="Lisa",fur="short"),
        sep="\n")

if __name__ == '__main__':
    main()



