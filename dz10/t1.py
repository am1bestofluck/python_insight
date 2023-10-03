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
        self.__shared = {'name': None, 'birthyear': None, 'weight': None}
        self.__unique_traits = {'bird': {'water_type': None},
                                'fish': {'water_type': None},
                                'cat': {'fur': None}
                                }

    def newPet(self, *args) -> list[Animal]:
        out = []
        for new in args:
            if new.lower() in self.validNames:
                out.append(self._gather_info(new.lower()))
            else:
                print(f"bad input: {new}")
        return out

    def _gather_info(self, pet_type: Pet) -> Fish | Bird | Cat:
        for i in self.__shared:
            self.__shared[i] = input(f"Input {i} of the {pet_type}")
        for j in self.__unique_traits[pet_type]:
            self.__unique_traits[pet_type][j] = input(f"Input {j} of the {pet_type}")
        match pet_type:
            case "bird":
                return Bird(birth_year=self.__shared['birthyear'],weight=self.__shared['weight'],
                            name=self.__shared['name'],
                            food=self.__unique_traits[pet_type][j])
            case "cat":
                return Cat(birth_year=self.__shared['birthyear'],weight=self.__shared['weight'],
                           fur=self.__unique_traits[pet_type][j],name=self.__shared['name'])
            case "fish":
                return Fish(birth_year=self.__shared['birthyear'],weight=self.__shared['weight'],
                            name=self.__shared['name'],water_type=self.__unique_traits[pet_type][j])


if __name__ == '__main__':
    a = PetFabric()
    q = a.newPet("cat", "dog", "fish", "soft")
    print(q)
