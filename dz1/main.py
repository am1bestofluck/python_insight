#!python 3.11

from numbers import Complex

"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки:
“Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


class Triangle:
    """
    Треугольник мы можем задать любой. Но __bool__ бросает False если стороны не подходят.
    """

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def __str__(self):
        return f"{self.__class__.__name__} with sides [{round(self.side_a, 2)}, " \
               +f"{self.side_b}, {self.side_c}]. {'Valid' if bool(self) else 'Invalid'}." \
               +f"{' '+self.notes()+'.' if self.__bool__() else ''}"

    def __bool__(self) -> bool:
        return False if self.side_a+self.side_b < self.side_c \
                        or self.side_a+self.side_c < self.side_b \
                        or self.side_c+self.side_b < self.side_a else True

    def notes(self) -> str:
        __note = "Default"
        match len({self.side_a, self.side_b, self.side_c}):
            case 2:
                __note = "Isosceles"
            case 1:
                __note = "Equilateral"
        return f"{__note} {self.__class__.__name__}"


class ComplexityCheck:
    __border_lower = 0
    __border_upper = 100001

    def __init__(self, number: int):
        if not isinstance(number, Complex):
            self.__number = self.reinput()
        elif number not in range(ComplexityCheck.__border_lower,ComplexityCheck.__border_upper):
            self.__number = self.reinput()
        else:
            self.__number = number
        self.__simple__ = None

    def __bool__(self):
        if self.__simple__ is not None:
            return self.__simple__
        for i in range(self.__number-1, 1, -1):
            if self.__number % i == 0:
                self.__simple__ = False
                return False

        self.__simple__ = True
        return True

    def __str__(self):
        return f"Number {self.__number}. {'Prime' if self.__bool__() else 'Composite'}."

    def reinput(self):
        number = None
        while number is None:
            buffer = input("Input number?")
            try:
                number = int(buffer)
            except ValueError:
                print("not a whole number")
                continue
            if number not in range(self.__border_lower+1, self.__border_upper):
                print(f"must be between  {self.__border_lower} and {self.__border_upper}.")
                number = None

        self.__simple__ = None
        return number


def main():
    sample = [Triangle(3, 3, 6), Triangle(2, 2, 2), Triangle(3, 4, 5), Triangle(1, 2, 30),
              ComplexityCheck(8), ComplexityCheck(7)]
    for i in sample:
        print(i)

    input_fail = ComplexityCheck(10**10)
    print(input_fail)

if __name__ == "__main__":
    main()
