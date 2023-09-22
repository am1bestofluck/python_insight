"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from os import chdir
from random import randint,randbytes,choices
from string import ascii_letters
def main(extention:str = ".rtf",
         min_name:int =6,max_name:int=42,
         min_size:int = 256,max_size:int=4096,
         file_count:int = 42):
    # chdir("t4")
    for file_ in range(file_count):
        name = "".join(choices(ascii_letters, k=randint(min_name, max_name))) + extention
        with open(name,"xb") as f:
            f.write(randbytes(n=randint(min_size,max_size)))


    pass

if __name__ == '__main__':
    main()
