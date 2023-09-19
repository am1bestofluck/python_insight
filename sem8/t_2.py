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

PATH = "t2_out.json"


def rewrite(d: dict):
    with open(PATH, "a") as f_o:
        json.dump(d, f_o, indent=2)


def read_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding="UTF-8") as file:
        dct = json.load(file)
    return dct


def update_dct(info: list, dct: dict) -> dict:
    dct.setdefault(str(info[2]), {})
    check = True
    for values in dct.values():
        if str(info[1]) in values.keys():
            check = False
    if check:
        dct[str(info[2])].update({str(info[1]): info[0]})
    return dct

# def reformat() -> dict:
#     global PATH
#     pass
#     # with open(PATH, 'a') as redo:
#     #     tmp = json.load(redo)


def whileT():
    global PATH
    while True:
        try:
            line = input("name? id? permissions?")
            tmp = line.split(" ")
            tmp[0] = tmp[0].title()
            tmp[1] = int(tmp[1])
            tmp[2] = int(tmp[2])
            d = dict()
            d[tmp[2]] = {tmp[0]: tmp[1]}
            # with open(PATH, "a") as f_o:
            #     json.dump(d, f_o, indent=2)
            read_json(PATH)
            update_dct(info=tmp,dct=d)
            rewrite(d)
        except IndexError:
            print("input error")


# json словарь с полномочиями
# как основные ключи
# дальше ещё словарь с id пользоватаеля
# в нём имя
# читаем из json; новый словарь update
# отдаём назад



if __name__ == '__main__':
    whileT()
