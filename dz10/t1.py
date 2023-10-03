"""Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""
from enum import Enum, auto
from sem10.t_5 import Fish, Bird, Cat, Animal


class Pet(Enum):
    bird = auto()
    fish = auto()
    cat = auto()


class PetFabric:
    def __init__(self):
        self.validNames = [e.name for e in Pet]

    def newPet(self, *args) -> list[Animal]:
        out = []
        for new in args:
            if new in self.validNames:
                out.append(self._gather_info(new))
            else:
                print(f"bad input: {new}")
        return out

    def _gather_info(self, pet_type: Pet) -> Fish | Bird | Cat:
        print(pet_type)
        return pet_type


if __name__ == '__main__':
    a = PetFabric()
    q = a.newPet("cat", "dog", "fish", "soft")
    print(q)
