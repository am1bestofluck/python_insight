import math
import re
from fractions import Fraction
from math import lcm


class FractionsCalc:
    __ops: [str, re.Pattern] = {
        "add": re.compile("\d*/\d*\+\d*/\d*"),
        "mult": re.compile("\d*/\d*\*\d*/\d*"),
        "div": re.compile("\d*/\d*/\d*/\d*"),
        "sub": re.compile("\d*/\d*-\d*/\d*")
    }

    def __init__(self, equation: str = None):
        self.equation_i = self.__check_string(equation)

    def __check_string(self, equation: str):
        return "error" if not isinstance(equation, str) or len(equation) > 200 else equation

    def get_next(self, equation: str):
        """следующая строка"""
        self.equation_i = self.__check_string(equation)

    def eval(self) -> str:
        """определяем кто есть кто"""
        buffer = None
        for i in FractionsCalc.__ops:
            if re.match(FractionsCalc.__ops[i], self.equation_i):
                buffer = i
                break
        if not buffer:
            return self.equation_i  # вернёт error если на входе чушь

        if buffer == "div":  # отдельный случай!
            temp = self.equation_i.split('/')
            first, second = (temp[0], temp[1]), (temp[2], temp[3])
        else:
            temp = re.split("[\+,\*,\-]", self.equation_i)
            first, second = (temp[0].split('/')[0], temp[0].split('/')[1]), \
                            (temp[1].split('/')[0], temp[1].split('/')[1])
        return self.__calc([first, second, buffer])

    def __calc(self, args: list) -> str:
        """

        :param args: [first:tuple[str,str],second:tuple[str,str],operation:str]
        :return: evaluation
        """
        # приводим к общему знаминателю сложение и вычитание а потом работаем с числителями как с натуральными
        # умножение - перемножаем этажи
        # деление-  переворачиваем дробь и умножаем
        out: tuple = (None,)
        assertion_args = [None, None]
        args[0], args[1] = (int(args[0][0]), int(args[0][1])), (int(args[1][0]), int(args[1][1]))
        match args[2]:
            case "add":
                args_m = self.__to_common_denominator(args[0], args[1])
                out = (args_m[0][0] + args_m[1][0], args_m[0][1])
                out = self.__reduce_fraction(out)
                assert Fraction(args[0][0], args[0][1]) + Fraction(args[1][0], args[1][1]) ==\
                       Fraction(out[0], out[1])
                pass
            case "sub":
                args_m = self.__to_common_denominator(args[0], args[1])
                out = (args_m[0][0] - args_m[1][0], args_m[0][1])
                assert Fraction(args[0][0], args[0][1]) - Fraction(args[1][0], args[1][1]) ==\
                       Fraction(out[0], out[1])
            case "mult":
                out = (args[0][0]*args[1][0],args[0][1]*args[1][1])
                out = self.__reduce_fraction(out)
                assert Fraction(args[0][0], args[0][1]) * Fraction(args[1][0], args[1][1]) ==\
                       Fraction(out[0], out[1])
                pass
            case "div":
                out = (args[0][0]*args[1][1],args[0][1]*args[1][0])
                out = self.__reduce_fraction(out)
                assert Fraction(args[0][0], args[0][1]) / Fraction(args[1][0], args[1][1]) ==\
                       Fraction(out[0], out[1])
                pass

        return f"{out[0]}/{out[1]}"

    def __reduce_fraction(self, fr_i: tuple) -> tuple:
        fr_m = None
        div = math.gcd(fr_i[0],fr_i[1])
        if div != 1:
            fr_m = (int(fr_i[0] / div), int(fr_i[1] / div))
        return fr_m if fr_m else fr_i

    def __to_common_denominator(self, fr1: tuple, fr2: tuple) -> list[tuple]:
        _lcm = math.lcm(fr1[1], fr2[1])
        return [(fr1[0] * int(_lcm / fr1[1]), _lcm), (fr2[0] * int(_lcm / fr2[1]), _lcm)]


def main():
    # glhf!
    a = FractionsCalc(equation="4/5+5/20")
    print(a.eval())
    a.get_next(equation="2/3*4/5")
    print(a.eval())
    a.get_next("10/3+2/3")
    print(a.eval())
    a.get_next("5/6-2/3")
    print(a.eval())
    a.get_next("30/10/3/1")
    print(a.eval())
    pass


if __name__ == '__main__':
    main()
