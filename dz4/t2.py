"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""
from pprint import pp


def main(**kwargs):
    out = dict()
    for item_name in kwargs:
        try:
            out[kwargs[item_name]] = item_name
        except TypeError:
            out[str(kwargs[item_name])] = item_name
    return out


if __name__ == '__main__':
    pp(main(b=[], o=set(), r=dict(),
            i=1, n=1.2, g=False, x=print, d=globals))
