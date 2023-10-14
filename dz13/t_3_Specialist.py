from dz13.t_3_Person import Person
from dz13.t_2_ex import InvalidIdError, UserException


class Specialist(Person):

    def __init__(self, firname: str, lasname: str, fatname: str, age: int, id_: int):
        """
        Сотрудники имеют также уникальный идентификационный номер (ID),
        который должен быть шестизначным положительным целым числом.
        """
        self.check_digit(id_, 10 ** 5, 10 ** 6 - 1)
        self._id = id_
        super().__init__(firname, lasname, fatname, age)

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, new_val):
        self.check_digit(new_val, 10 ** 5, 10 ** 6 - 1)
        self._id = new_val

    @staticmethod
    def check_digit(item: int, lower: int = 0, upper: int = 100):
        if not isinstance(item, int) or item not in range(lower, upper + 1):
            raise InvalidIdError(item, lower, upper)

    def get_level(self):
        """Добавить метод get_level в класс Employee, который будет возвращать уровень
сотрудника на основе суммы цифр в его ID (по остатку от деления на 7)."""
        return self.id_ % 7

    def __str__(self):
        return "Correct"


def main():
    for i in [
        ["S", "D", "F", 34, 700001],
        ["", "D", "F", 34, 700001],
        ["S", "", "F", 34, 700001],
        ["S", "D", "", 34, 700001],
        ["S", "D", "F", -34, 700001],
        ["S", "D", "F", 34, 70001]
    ]:
        try:
            print(Specialist(*i))
        except UserException as e:
            print(e)


if __name__ == '__main__':
    main()
