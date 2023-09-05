"""
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
from random import sample
from string import printable
from pprint import PrettyPrinter

main_out = PrettyPrinter(compact=True)


class Container:
    def __init__(self, name: str, items: set[str]):
        self.name = name
        self.items = items

    def __add__(self, item: str):
        self.items.add(item)

    def __str__(self):
        return f"Набор вещей {self.name},из {self.items}"


def main(*, friends: int, items_pool: int, items_per_friend: int):
    """
    :param friends: кол-во друзей
    :param items_pool: сколько вообще есть вещей <= 100
    :param items_per_friend: сколько случайных вещей из items_pool взял друг

    :return: dict[Container]
    """
    assert items_per_friend <= items_pool
    overall_items = dict()
    for i in range(friends):
        overall_items[i] = set(i for i in sample(range(items_pool), k=items_per_friend))
    out = {
        "unique": set(),
        "shared": set()
    }
    for i in range(friends):
        out[f"forgotten_{i}"] = set()
    temp_diff = set()
    temp_shared= set()
    buffer_shared = overall_items[0]
    for i in range(friends):
        try:
            out["shared"] = overall_items[i] if not out["shared"] else out["shared"].intersection(overall_items[i])
        except KeyError:
            pass

        out["unique"] = overall_items[i].difference(temp_diff)
        temp_diff = temp_diff.union(overall_items[i])
    return overall_items, out


if __name__ == '__main__':
    print(main_out.pprint(main(friends=3, items_per_friend=25, items_pool=50)))
