from dz13.t_2_ex import InvalidTextError, InvalidNumberError, UserException


class Person:
    def __init__(self, firname: str, lasname: str, fatname: str, age: int):
        """
        Фамилия (строка, не пустая)
        Имя (строка, не пустая)
        Отчество (строка, не пустая)
        Возраст (целое положительное число)
        """
        Person.check_string(firname, lasname, fatname)
        Person.check_digit(age)
        self.fir_name = firname
        self.las_name = lasname
        self.fat_name = fatname
        self.age = age

    @staticmethod
    def check_digit(item: int, lower: int = 0, upper: int = 100):
        if not isinstance(item, int) or item not in range(lower, upper+1):
            raise InvalidNumberError(item)

    @staticmethod
    def check_string(*args):
        for i in args:
            if not isinstance(i, str) or i == "":
                raise InvalidTextError(str(type(i)))

    def birthday(self):
        """Добавить метод birthday в класс Person,
который будет увеличивать возраст человека на 1 год."""
        self.age += 1

    def __str__(self):
        return "correct"


def main():
    for i in [
        ["S", "D", "F", 34],
        ["", "D", "F", 34],
        ["S", "", "F", 34],
        ["S", "D", "", 34],
        ["S", "D", "F", -34]
    ]:
        try:
            print(Person(*i))
        except UserException as e:
            print(e)


if __name__ == '__main__':
    main()
