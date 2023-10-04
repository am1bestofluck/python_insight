"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""

from getpass import getuser
from datetime import datetime


class MyString(str):
    def __init__(self, content: str):
        self.content = content
        self.author = getuser()
        self.creation_time = datetime.now()


if __name__ == '__main__':
    a = MyString("hi")
    print(vars(a))
    print(a.__dict__)
