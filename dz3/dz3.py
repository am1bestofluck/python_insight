"""
Создайте словарь со списком вещей для похода в качестве ключа
 и их массой в качестве значения. Определите какие вещи влезут
  в рюкзак передав его максимальную грузоподъёмность.
   Достаточно вернуть один допустимый вариант.
    *Верните все возможные варианты комплектации рюкзака.


    https://habr.com/ru/articles/479816/
"""
from random import sample, choice, choices
from string import ascii_lowercase
from itertools import permutations
from pprint import PrettyPrinter

def main(bag_volume_i: int, items: dict):
    if sum(items.values()) < bag_volume_i:
        return items

    out = set()
    for i in permutations(items):
        option = dict()
        temp_sum = 0
        counter = 0
        while temp_sum < bag_volume_i:
            option[i[counter]] = items[i[counter]]
            temp_sum += items[i[counter]]
            counter +=1
        out.add(str(option))
    return out


if __name__ == '__main__':
    items_qua = choice(range(1, 10))
    max_weight_per_item = 20
    bag_volume = choice(range(1, 40))

    names = sample(ascii_lowercase, k=items_qua)
    weights = choices(range(1, max_weight_per_item), k=items_qua)
    all_items = dict()
    for i in range(items_qua):
        all_items[names[i]] = weights[i]

    print(f"{all_items=}")
    print(f"{bag_volume=}")
    print(f"out={str(main(bag_volume, all_items))}")
