"""
В модуль с проверкой даты добавьте возможность запуска
 в терминале с передачей даты на проверку.
"""

from sys import argv

from sem6 import timeout_7


def main():
    if len(argv) > 1:
        print("надстройка исключительно для того чтобы работать БЕЗ консоли")
        exit(1)
    argv.append(input("DD.MM.YYYY ?"))
    print(timeout_7.not_main())

if __name__ == '__main__':
    main()