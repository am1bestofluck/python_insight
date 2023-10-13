"""
Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError,
 которые будет вызываться, когда текст не является строкой
  или является пустой строкой.

И InvalidNumberError, которое будет вызываться, если число не является
положительным целым числом или числом с плавающей запятой.
"""
from dz13.t_2_sample import Archive
from dz13.t_2_ex import InvalidNumberError, InvalidTextError, UserException


class ArchiveExtended(Archive):
    def __init__(self, text: str, num: int):
        if not isinstance(text, str) or text == "":
            raise InvalidTextError(str(type(text)))
        if isinstance(num, float) or num < 0:
            raise InvalidNumberError(num)
        super().__init__(text, num)


if __name__ == '__main__':
    a = ArchiveExtended("1", 2)
    a = ArchiveExtended("2", 3)
    print(a)
    try:
        a = ArchiveExtended("", 3)
    except InvalidTextError as e:
        print(e)

    try:
        a = ArchiveExtended(3, 3)
    except InvalidTextError as e:
        print(e)
    try:
        a = ArchiveExtended("cool", 100.0)
    except InvalidNumberError as e:
        print(e)
    try:
        a = ArchiveExtended("cool", -300)
    except InvalidNumberError as e:
        print(e)
    try:
        a = ArchiveExtended("", -800)
    except UserException as e:
        print(e)
