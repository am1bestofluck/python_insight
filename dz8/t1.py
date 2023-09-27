"""
Напишите функцию, которая получает на вход директорию
 и рекурсивно обходит её и все вложенные директории. #os.walk
  Результаты обхода сохраните в файлы json, csv и pickle. #Node
Для дочерних объектов указывайте родительскую директорию. #Path?
Для каждого объекта укажите файл это или директория. #isdir
Для файлов сохраните его размер в байтах,
 а для директорий размер файлов в ней
  с учётом всех вложенных файлов и директорий.

"""
import os

from format import Format
# искать размер папки своей головой оказалось сложнее чем хотелось бы.
# https://www.tutorialspoint.com/How-to-calculate-a-directory-size-using-Python
# таааакс. Раз уж мы будем много добавлять, а читать - 1 раз и то не факт
# то можно сделать односвязный список потому что на добавление o(1).

from pprint import pp
from pathlib import Path
from linked_list import LinkedList
from extractor import Extractor


def main(path_i: Path):
    a = LinkedList()
    a.build_by_dir(path_i)
    b = Extractor(a,path_i.absolute())
    b.all_reports()


if __name__ == '__main__':
    main(Path("."))
