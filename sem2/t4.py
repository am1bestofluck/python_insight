"""
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""
from math import sqrt
def main(a,b,c):
    #ax**2+bx+c = 0
    discriminant = b**2 - 4*a*c
    if discriminant>=0:
        raise ValueError("Мы фокусируемся на негативах")
    d_ = complex(discriminant,1)
    print(d_)
    x1=-(b+sqrt(d_))/2*a
    x2=-(b-sqrt(d_))/2*a
    print(x1,x2)


