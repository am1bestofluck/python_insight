"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
 которые вы уже решали. Превратите функции в методы класса,
  а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
"""
from pathlib import Path


class HexConverter:
    def __init__(self, item: int = None):
        self.__item = item

    def get_next(self, new_item: int = None):
        self.__item = new_item

    def convert(self):
        if self.__item is None:
            return
        result = ""
        div = abs(self.__item)
        if div == 0:
            return "0x0"  # если это неок - переделаю
        while div > 0:
            div, mod = divmod(div, 16)
            match mod:
                case 10:
                    mod = "a"
                case 11:
                    mod = "b"
                case 12:
                    mod = "c"
                case 13:
                    mod = "d"
                case 14:
                    mod = "e"
                case 15:
                    mod = "f"
                case _:
                    mod = str(mod)
            result = mod + result
        return f"{'' if self.__item >= 0 else '-'}0x{result}"

class PathSplitter:
    def __init__(self,path_i:Path):
        self.path = path_i.absolute().as_posix()
    def new_route(self,new_path:Path):
        self.path = new_path.absolute().as_posix()

    def split(self):
        *w, n_e = self.path.split("/")
        n, e = n_e.split(".")

        return (w, n, e)
if __name__ == '__main__':
    a = HexConverter()
    for i in range(17):
        a.get_next(i)
        print(a.convert(), end=" ")
    print()
    b =PathSplitter(Path("t2.py"))
    print(b.split())
    b.new_route(Path("t1.py"))
    print(b.split())
