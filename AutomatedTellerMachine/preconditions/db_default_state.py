"""
Заполняем базу дефолтными значениями
"""
# from decimal import Decimal, getcontext
import json

import mysql.connector


def notes_terminals():
    for i in range(1, 11):
        yield i, f"place #{i}", 30_000


def main():
    with open('../creds/credentials.json') as src:
        creds = json.load(src)
        with mysql.connector.connect(user=creds['user'],
                                     password=creds['pw'],
                                     host=creds['host'], database='terminals') as core:
            crs = core.cursor()
            expr = "INSERT INTO terminal_units(number,location,balance) VALUES (%s, %s, %s)"
            crs.executemany(expr, list(notes_terminals()))
            expr = "INSERT INTO cards (card_number) VALUES ('%s')"
            crs.executemany(expr, [(i,) for i in range(1234_0000_0000_0000, 1234_0000_0001_0001)])
            core.commit()


if __name__ == '__main__':
    main()
