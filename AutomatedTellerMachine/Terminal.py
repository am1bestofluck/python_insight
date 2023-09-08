import json
from pathlib import Path
import mysql.connector


class Terminal:
    """
    Наш терминал.
    Номера терминалов
    с   1
    по  10

    """
    __cnt = mysql.connector
    __creds = Path("./creds/credentials.json")
    __number = Path('./creds/terminal.json')

    def __init__(self):
        self.__number = self.__get_terminal_id()
        self.__balance = self.__get_vault()

    def __get_terminal_id(self):
        with open(Terminal.__number, 'r') as src:
            id = json.load(src)['id']
        return id

    def __ask_base(self, command: str):
        with open(Terminal.__creds, 'r') as src:
            creds = json.load(src)
            with Terminal.__cnt.connect(user=creds["user"], password=creds["pw"],
                                        host=creds["host"], database=creds["database"]) as srv:
                crs = srv.cursor()
                crs.execute(command)
                return crs.fetchall()

        # cnx = mysql.connector.connect(user='root', password='AccountsandRoles1!',
        #                                       host='localhost',
        #                                       database='terminals')
        return command

    def __get_vault(self):
        return self.__ask_base(f"SELECT balance FROM terminals WHERE id = {self.__number};")[0]

    def __repr__(self):
        return f"Терминал, в кассе {self.__get_vault()}."


if __name__ == '__main__':
    a = Terminal()
    print(a)
