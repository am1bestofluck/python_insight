"""
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

def main():
    a ="sadfsgsdadfghgfs"
    # out = {}
    out = {i:ord(i) for i in a}
    out1= (ord(i) for i in a)
    return out,out1

if __name__ == '__main__':
    print(main(),sep="\n")