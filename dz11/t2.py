"""
Разработайте программу для хранения и управления текстовыми и числовыми записями.
Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:

Класс Archive должен иметь следующие атрибуты:

archive_text (list): Список архивированных текстовых записей.
archive_number (list): Список архивированных числовых записей.
text (str): Текущая текстовая запись, которую нужно добавить в архив.
number (int или float): Текущая числовая запись, которую нужно добавить в архив.
Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.

Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую и числовую запись и сохраняет их как текущие записи для добавления в архив.

Класс Archive должен реализовать методы
__str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.
"""

# https://python-patterns.guide/gang-of-four/singleton/
IN = """
archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)"""

OUT = """
Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]"""


class Archive:
    _instance = None
    full_archive_text = []
    full_archive_number = []
    archive_text = []
    archive_number = []

    def __new__(cls, text: str, number: "int | float"):
        if cls._instance is None:
            cls._instance = super(Archive,cls).__new__(cls)
        cls._instance.text = text
        cls._instance.number = number
        Archive.full_archive_text.append(text)
        Archive.full_archive_number.append(number)
        Archive.archive_text = Archive.full_archive_text[0:len(Archive.full_archive_text)-1]
        Archive.archive_number = Archive.full_archive_number[0:len(Archive.full_archive_number)-1]
        return cls._instance

    # def __init__(self, text: str, number: int | float):
    #     self.text = text
    #     self.number = number
    #     Archive.archive_text.append(text)
    #     Archive.archive_number.append(number)

    def __str__(self):
        q, w = self.archive_text, self.archive_number
        return f"Text is {self.text} and number is {self.number}. Also {q} and {w}"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1)
    archive2 = Archive("Запись 2", 3.14)
    print(archive2)
    print(archive2.archive_text)
    print(archive1.archive_number)
