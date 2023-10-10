class Parent:
    __slots__ = "name", "is_cool"

    def __init__(self, name: str, is_cool: bool):
        self.name = name
        self.is_cool = is_cool


class Child(Parent):
    __slots__ = "age",

    def __init__(self, *args):
        self.age = args[0]
        super(Child, self).__init__(args[1], args[2])


if __name__ == '__main__':
    A = Child("A", True, 23)
    A.eyes = "Green"  # должно вылететь с ошибкой потому что нет в __slots__... или нет?
    print("не вылетело!")
