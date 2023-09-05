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
    d_ = complex(round(sqrt(abs(discriminant)),2),1)
    print(d_)
    x1=(-b+d_)/2*a
    x2=(-b-d_)/2*a
    print(x1,x2)



