"""
Заполняем базу дефолтными значениями
"""
# from decimal import Decimal, getcontext
from random import choice
import json

import mysql.connector

CARD_NUMBERS = range(1234_0000_0000_0000, 1234_0000_0001_0001)


def get_card_ids(crs: mysql.connector.cursor) -> tuple[tuple]:
    """достаём номера и id -первичные ключи карт из базы
    нюанс - карты уже должны там быть"""
    expr = "SELECT card_number,id FROM terminals.cards"
    crs.execute(expr)
    return crs.fetchall()


def notes_terminals():
    """состояние банкоматов( №, где, сколько в кассе)"""
    for i in range(1, 11):
        yield i, f"place #{i}", 30_000


def card_balances(crs: 'cursor'):
    """рандомим у.е. на карточках """
    for num in get_card_ids(crs):
        yield num[1], choice(range(0, 10000, 100))


def main():
    global CARD_NUMBERS
    with open('../creds/credentials.json') as src:
        creds = json.load(src)
        with mysql.connector.connect(user=creds['user'],
                                     password=creds['pw'],
                                     host=creds['host'], database='terminals') as core:
            crs = core.cursor()
            crs.execute("DROP SCHEMA IF EXISTS terminals;")
            crs.execute("CREATE SCHEMA `terminals`;")
            crs.execute("use `terminals`;")
            crs.execute("CREATE TABLE cards(id SERIAL, card_number CHAR(16) UNIQUE,is_blocked BIT, PRIMARY KEY(id))")
            crs.execute("CREATE TABLE card_balances (id SERIAL, card_id BIGINT UNSIGNED,"
                        "balance DECIMAL(12,2),PRIMARY KEY(id),FOREIGN KEY "
                        "(card_id) REFERENCES cards(id) );")
            crs.execute("CREATE TABLE pins(id SERIAL, card_id BIGINT UNSIGNED, pin CHAR(5), "
                        "PRIMARY KEY(id),FOREIGN KEY (card_id) REFERENCES cards(id));")
            crs.execute("CREATE TABLE terminal_units (id SERIAL,number TINYINT, location TINYTEXT, "
                        "balance DECIMAL(12,2), PRIMARY KEY(id));")
            expr = "INSERT INTO terminal_units(number,location,balance) VALUES (%s, %s, %s)"
            crs.executemany(expr, list(notes_terminals()))
            expr = "INSERT INTO cards (card_number,is_blocked) VALUES ('%s', %s)"
            crs.executemany(expr, [(i, 0) for i in CARD_NUMBERS])
            # card_balances (id SERIAL, card_id BIGINT UNSIGNED, balance DECIMAL(12,2),
            expr = "INSERT INTO card_balances(card_id, balance) VALUES (%s, %s)"
            crs.executemany(expr, list(card_balances(crs)))
            # CREATE TABLE pins(id SERIAL, card_id BIGINT UNSIGNED, pin BIGINT,
            expr = "INSERT into pins(card_id, pin) VALUES (%s, %s)"
            crs.executemany(expr, list(card_pins(crs)))
            core.commit()
    print("ok")


def card_pins(crs: 'cursor'):
    for num in get_card_ids(crs):
        yield num[1], str(num[0])[-5:]


if __name__ == '__main__':
    main()
