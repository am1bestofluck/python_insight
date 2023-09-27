"""
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
"""
# Тааак. А шо мы собственно делали?
# Самое свежее воспоминание: мы обходили папку и указывали тип и размер файлов.
try:
    from t1 import main as inspect_dir
except ImportError:
    from .t1 import main as inspect_dir
# Дальше в программе: типа база данных с логинами-паролями
from sem8 import input_loop as prepare_security_breach
# и уже потом мы нашу базу красили в белый цвет с чёрными пятнами и в чёрный с белыми
from sem8 import base_to_json, pickle_to_csv,csv_as_pickle
# ... и конвертировали json'ы в пиклы по папкам
from sem8 import jsons_to_pickle

__all__ = ['inspect_dir', 'prepare_security_breach', 'base_to_json',
           'jsons_to_pickle', "pickle_to_csv",'csv_as_pickle']

if __name__ == '__main__':
    print("ok")
