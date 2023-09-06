"""
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:+
✔ Какие вещи взяли все три друга+
✔ Какие вещи уникальны, есть только у одного друга+
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует+
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.+
"""
from pprint import PrettyPrinter
from random import sample

main_out = PrettyPrinter(compact=True)


class Container:  # не пригодился класс то =\ =)
    def __init__(self, name: str, items: set[str]):
        self.name = name
        self.items = items

    def __add__(self, item: str):
        self.items.add(item)

    def __str__(self):
        return f"Рюкзак {self.name}"

    def __repr__(self):
        return f"Набор вещей {self.name},из {self.items!r}"


def main(*, friends: int, items_pool: int, items_per_friend: int) -> dict[int, Container | tuple]:
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
    temp_shared = set()
    buffer_shared = overall_items[0]
    for i in range(friends):
        try:
            out["shared"] = overall_items[i] if not out["shared"] else out["shared"].intersection(overall_items[i])
        except KeyError:
            pass

        out["unique"] = overall_items[i].difference(temp_diff)
        temp_diff = temp_diff.union(overall_items[i])
        other_friends = list(range(friends))
        other_friends.remove(i)
        temp_shared_by_2 = set()
        for j in other_friends:
            temp_shared_by_2 = overall_items[j] if not temp_shared_by_2 else temp_shared_by_2.intersection(
                overall_items[j])
        out[f"forgotten_{i}"] = temp_shared_by_2.difference(overall_items[i])
    for i in range(friends):
        out[i] = Container(i, overall_items[i])
    return out


if __name__ == '__main__':
    for counter in [3, 5, 2]:
        print(main_out.pprint(main(friends=counter, items_per_friend=25, items_pool=50)))
        print("\n" * 3)
