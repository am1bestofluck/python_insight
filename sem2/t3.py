"""
✔Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔Диаметр не превышает 1000 у.е.
✔Точность вычислений должна составлять не менее 42 знаков после запятой.

"""
from math import  pi
import  decimal

def main():
    while True:
        try:
            radius = int(input("R?"))
            if radius not in range(501):
                raise ValueError
            break
        except ValueError:
            continue
    decimal.getcontext().prec = 43
    print(decimal.Decimal(pi) * decimal.Decimal(radius) ** 2)
    print(2 * decimal.Decimal(pi) * decimal.Decimal(radius))
