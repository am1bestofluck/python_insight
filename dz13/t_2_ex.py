class UserException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class InvalidTextError(UserException):
    errType = "Несоответствие типов. Ожидали <class 'str'>, получили "
    errVal = "Пустые строки запрещены."

    def __init__(self, got_type: str):
        self.gt = got_type
        self.errType = self.errType+self.gt

        pass

    def __str__(self):
        return self.errVal if self.gt == "<class 'str'>" else self.errType


class InvalidNumberError(UserException):
    def __init__(self, got: int):
        self.got = got

    def __str__(self):
        return f"Разрешены натуральные числа. Получено: {self.got}"


if __name__ == '__main__':
    # raise InvalidTextError
    # raise InvalidNumberError
    pass


class InvalidIdError(InvalidNumberError):
    def __init__(self, got: int, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
        super().__init__(got)

    def __str__(self):
        return super().__str__() + f". In bounds of {self.lower}..{self.upper}"
