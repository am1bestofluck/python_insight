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
        self._access_level = None

    @property
    def get_all(self) -> list[KnownUser]:
        return get_them_all(SAMPLE)

    def auth(self, name, id_: int):
        self.logout()
        for i in self.get_all:
            if i.name == name and i.id == id_:
                print(f"Logged as {i.name}, access level: {i.access}")
                self._access_level = i.access

    def add_user(self, name: str, id: int, permissions: int):
        if self._access_level is None:
            raise AccessException("Сперва авторизуйтесь")
        if permissions < int(self._access_level):
            raise LevelException(
                f"Нельзя создать более привилегированного пользователя."+ \
                f" хотим создать: {permissions}; наши права: {self._access_level} ")
        tmp = KnownUser(name=name, id_=id, access=permissions)
        print(tmp, "created")
        self.logout()

    def logout(self):
        print("logging out!")
        self._access_level = None


if __name__ == '__main__':
    a = Auth()
    b = Auth()
    print(a == b)
    a.auth(name="A", id_=1)
    a.add_user(name="Ok", id=500, permissions=6)
    a.auth(name="A", id_=1)
    a.add_user(name="Err", id=500, permissions=1)
