"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def main():
    sing = True
    swim = True
    slay = True
    cases = False
    birds = False
    s = True
    case = 0
    bird = 0
    item = None
    for item in locals().items():
        if item[0].endswith('s') and item[0] != 's':
            locals[item[0][:-1]] = item[1]
            locals[item[0]] = None
    print()


if __name__ == '__main__':
    main()
