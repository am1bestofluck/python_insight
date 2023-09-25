"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл. # записываем в жсон
Пользователи группируются по уровню доступа. # перезаписываем файлик каждый раз

Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""
import json
import sys

PATH = "t2_out.json"
SCOPES = range(8)


def input_loop():
    while True:
        base: dict = read_j()
        new_user = get_input(base)
        base = update_dict(base,new_user)
        write_j(base)
    return


def read_j():
    with open(PATH, "r") as b4:
        try:
            return json.loads("".join(b4.readlines()),parse_int=int)
        except json.JSONDecodeError:  # пустой? коррапченый?
            return {}


def write_j(newdict: dict):
    with open(PATH, "w") as after:
        after.write(json.dumps(newdict,indent=1))
    return

def update_dict(dict_old:dict[dict],variant:dict) -> dict:
    mask = list(variant.keys())[0]
    hateit = str(mask)
    if hateit not in dict_old:
        dict_old[hateit]= variant[mask]
    else:
        dict_old[hateit].update(variant[mask])
    return  dict_old

def get_input(prevdata: dict) -> dict:
    keys_ = []
    for i in prevdata:
        for step in i:
            keys_.append(step)
    keys_ = map(int, keys_)
    while True:
        tmp = input("name id access").split()
        try:
            if not tmp:
                raise SystemExit
            if len(tmp) != 3:
                raise IndexError
            if tmp[0].isdigit():
                raise AttributeError("Число в нулевом индексе")
            if int(tmp[1]) in keys_:
                raise AttributeError("такой id уже есть")
            if int(tmp[2]) not in SCOPES:
                raise AttributeError("такого уровня полномочий нет")

            return {int(tmp[2]): {int(tmp[1]): tmp[0].title()}}

        except AttributeError as exc:
            print(exc.args[0])
        except (ValueError, IndexError):
            print("Строка число число")

        except SystemExit as bye:
            print("bye")
            sys.exit(0)


if __name__ == '__main__':
    input_loop()
