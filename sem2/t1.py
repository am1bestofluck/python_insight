"""
Создайте в переменной data список значений разных типов перечислив 
их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
\n\n✔порядковый номер начиная с единицы
\n\n✔значение \n\n✔адрес в памяти
\n\n✔размер в памяти \n\n✔хэш объекта
n✔результат проверки на целое число только если он положительный
\n✔результат проверки на строку только если он положительный Добавьте в список повторяющиеся элементы и сравните на результаты.

20:16

"""
import sys
def main():
    a = [None,True,2,3.0,'4']
    for i in range(len(a)):
        print(i+1)
        print(a[i],id(a[i]))
        print(sys.getsizeof(a[i]),hash(a[i]))
        if isinstance(a[i],int|float): print(type(a[i]))
        input("next")