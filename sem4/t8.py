"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
sing = False
swim = False
slay = False
cases = "cases"
birds = "birds"
s = None


def main():
    items = [i for i in globals() if
             not i.startswith('__') and i.endswith('s') and len(i) > 1]
    for item in items:
        globals()[item[:-1]] = globals()[item]
        globals()[item] = None


def local_case():
    cats = "cats"
    dogs = "dogs"
    noway = False
    s = 3
    items = [i for i in locals() if
             i.endswith('s') and len(i) > 1 and
             not i.startswith('__')]
    for item in items:
        locals()[item[:-1]] = locals()[item]
        locals()[item] = None
    print("А ват на локальном уровне, всё интереснее.",
          "Явно указывая словарь получаем результат",
          f"{locals()['cat']=}, {locals()['dog']=}",
          sep="\n\r")
    try:
        print(cat, dog)
    except NameError:
        print("а само по себе - чудо не происходит :))",
              "Может по-этому на семинаре и не получилось самому сделать?",
              "(делал как раз на локальном этаже)",sep="\n")


if __name__ == '__main__':
    print("Писал по памяти, не заглядывая в сам семинар.")
    main()
    print(f"По глобальным значениям, сопротивления особо не втретил,",
          f"{cases=}, {birds=}, {case=}, {bird=}.", sep="\n")
    local_case()
