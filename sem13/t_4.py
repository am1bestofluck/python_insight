"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
from pathlib import Path
import json

SAMPLE = Path("../sem8/t2_out.json")


class KnownUser:
    def __init__(self, name, id_, access):
        self.name = name
        self.id = id_
        self.access = access

    def __str__(self):
        return f"K.U. {self.id}/{self.name}:{self.access}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other: 'KnownUser'):
        return other.id == self.id and other.name == self.name


def get_them_all(p: Path):
    out: list[KnownUser] = []
    with open(p) as f:
        tmp = json.loads(f.read())
        for group in tmp:
            tmp1 = tmp[group]
            for usr in tmp1:
                out.append(KnownUser(name=tmp1[usr], id_=int(usr), access=group))
    return out


if __name__ == '__main__':
    print(
        get_them_all(SAMPLE)
    )
