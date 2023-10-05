"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""


# рузкий на отличьна

class Archive:
    _prev_int = []
    _prev_str = []

    def __init__(self, who_wrote: str, this_task: int):
        self.w = who_wrote
        self.t = this_task
        Archive._prev_str.append(who_wrote)
        Archive._prev_int.append(this_task)
    @classmethod
    def test(cls):
        """asd"""
        return
    @classmethod
    def get_protected(cls):
        """blah"""
        return cls._prev_str, cls._prev_int


if __name__ == '__main__':
    a = Archive("lobsters", 3)
    print(a.get_protected())
    b = Archive("fish", 5)
    print(b.__dict__)
    print(a.get_protected())
