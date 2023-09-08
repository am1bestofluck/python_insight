import mysql.connector

def main():
    with mysql.connector.connect(user='root', password='AccountsandRoles1!',
                                             host='localhost',
                                             database='terminals') as core:
        print(core.is_connected())
        print('ok')
    print(core.is_connected())

if __name__ == '__main__':
    main()
