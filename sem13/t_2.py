"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def default_dict_(dict_: dict, key_: any, default_: any):
    try:
        return dict_[key_]
    except KeyError:
        print(f"No  value on {key_}. Returning default!")
        return default_


if __name__ == '__main__':
    a = {1: 1, 2: 2, 3: 3}
    print(default_dict_(a, 100, 5))
