import sys

import mysql.connector


def main():
    cnx = mysql.connector.connect(user='root', password='AccountsandRoles1!',
                                  host='localhost',
                                  database='terminals')
    cnx.close()
    print('ok')


if __name__ == '__main__':
    main()
