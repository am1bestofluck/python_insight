"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы. #enumerate
✔ Слова выводятся отсортированными согласно кодировки Unicode. # default
✔ Текст выравнивается по правому краю так, чтобы у самого длинного f"<>"
слова был один пробел между ним и номером строки. len()
"""

def main():
    a = "Per aspera ad astra"
    lst = a.split()
    len_max = max(lst,key=len)
    len_max = len(len_max)+1
    lst.sort()
    for ham,eggs in enumerate(lst,1):
        print(f"{ham}.{eggs :>{len_max}}")