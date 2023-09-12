import json
from pathlib import Path

import mysql.connector

from Card import Card


class Terminal:
    """
    Наш терминал.
    Допустимые номера терминалов с 1 по 10, но этот всегда будет первый потому что его
    номер берётся из файла
    """
    __cnt = mysql.connector
    __creds = Path("./creds/credentials.json")
    __number = Path('./creds/terminal.json')

    def __init__(self):
        self.__number = self.__get_terminal_id()
        self.__balance = self.__get_vault()
        self.__serviced_card: Card = None

    def __on_screen(self, msg: str):
        """Это сообщение увидит пользователь"""
        return f"На экране высветилось:'{msg}'"

    def __get_terminal_id(self):
        """получаем id терминала из файла"""
        with open(Terminal.__number, 'r') as src:
            id_ = json.load(src)['id']
        return id_

    def __ask_base(self, command: str):
        """Обёртка для обращений к sql"""
        with open(Terminal.__creds, 'r') as src:
            creds = json.load(src)
            with Terminal.__cnt.connect(user=creds["user"], password=creds["pw"],
                                        host=creds["host"], database=creds["database"]) as srv:
                crs = srv.cursor()
                crs.execute(command)
                return crs.fetchall()

    def __get_vault(self):
        """Получаем с базы текущую наличку в кассе"""
        return self.__ask_base(f"SELECT balance FROM terminal_units WHERE id = {self.__number};")[0]

    def __check_card_relation(self, card_number: int) -> bool:
        """Проверяем наша ли это карта"""
        return bool(self.__ask_base(f"SELECT id from cards where card_number = {card_number}"))

    def __get_pin(self, card_i: Card) -> bool:
        """вводим пин карты"""
        # Не комфортно хранить пароль тут, даже во временной переменной;
        # в идеале нужно отправить ввод туда и сверить... как -не знаю :)
        attempts = 3
        secret = hash(self.__ask_base("".join(["SELECT pin from terminals.pins join cards on cards.id = ",
                                               f"terminals.pins.card_id where terminals.cards.card_number = {card_i.get()}"]))
                      [0][0])
        while attempts:
            print(self.__on_screen("Тссс.. :) Введите пин-код карты"))
            if hash(input()) == secret:
                temp_pw = None
                return True
            else:
                attempts -= 1
                print(self.__on_screen(f"Осталось {attempts} {'попытка' if attempts == 1 else 'попытки'}."))
        temp_pw = None
        c_id = self.__ask_base(f"SELECT id from cards where card_number = {card_i.get()}")
        self.__ask_base(f"update cards set is_blocked = b'1' where id = {c_id}")
        return False

    def __card_blocked(self, card_i: Card) -> bool:
        """Проверяем заблокирована ли карта"""
        expr = f"SELECT is_blocked FROM cards where card_number = {card_i.get()}"
        return bool(self.__ask_base(expr)[0][0])

    def __repr__(self):
        return f"Терминал #{self.__get_terminal_id()}, в кассе {str(self.__get_vault()[0])}."

    def get_card(self, card_i: Card):
        """Первая часть рутины: определяемся с картой"""
        if not self.__check_card_relation(card_i.get()):
            print(self.__on_screen("Карточка не обслуживается. Заберите."))
            return
        if self.__card_blocked(card_i) or not self.__get_pin(card_i):
            print(self.__on_screen("\n".join(["Карта заблокирована. Заберите.",
                                              "Для разблокировки обратитесь в техподдержку."])))

        print(self.__on_screen("Добрый здрасьте. Чем можем помочь?"))
        self.__serviced_card = card_i
        self.loop()

    def loop(self):
        """Вторая часть рутины. Repl с авторизованной картой"""
        while self.__serviced_card:
            match input("Command?").lower():
                case "q":
                    self.__serviced_card = None  # типа вернули карту...
                    print(self.__on_screen("Благодарим за внимание. До скорого!"))
                case "add":
                    print(self.__on_screen("Внесите сумму в ящик для обмена"))
                case "cash":
                    print(self.__on_screen("Введите сумму к обналичиванию"))
                case "pay":
                    print(self.__on_screen("Оплачиваем абстрактные услуги"))


if __name__ == '__main__':
    terminal = Terminal()
    card = Card(1234000000000000)
    print(card, card.get_pin(), sep="\n")
    terminal.get_card(card)
