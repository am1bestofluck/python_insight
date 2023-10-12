"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.

"""
from sem13.t_4 import get_them_all, KnownUser, SAMPLE
from sem13.t_3 import AccessException, LevelException


class Auth:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Auth, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    @property
    def get_all(self):
        return get_them_all(SAMPLE)

    def auth(self, name, id):
        pass

    def add_user(self):
        pass


if __name__ == '__main__':
    a = Auth()
    b = Auth()
    a == b
