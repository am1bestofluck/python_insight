"""
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""
from random import choice
def input_(a,b,c,*args):
    return {b:a,c:args}

if __name__ == '__main__':
    buff = ""
    buff =buff.join([f"{choice(range(i))}/" for i in range(1,choice(range(10,20)))])[:-1].split("/")
    buff = [int(i) for i in buff]
    print(buff)
    print(input_(*input("1/...").strip('/').split('/')))

# def main():
#     buff = ""
#     # buff =buff.join([f"{choice(range(i))}/" for i in range(1,choice(range(10,20)))])[:-1].split("/")
#     # 1,2 - ключи 0 значение для первого >>
#     out = dict()
#     out[buff[1]] = None
#     out[buff[2]] = None
#     out[buff[1]] = out[buff[0]]