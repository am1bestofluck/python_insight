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
import sys
from pathlib import Path
from os.path import getsize


# таааакс. Раз уж мы будем много добавлять, а читать - 1 раз и то не факт
# то можно сделать односвязный список потому что на добавление o(1).
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: "Node"):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __len__(self):
        out = 0
        node: Node = self.head
        while node:
            node = node.next
            out += 1
        return out

    def __iter__(self):
        self.walk_node: Node = self.head
        return self

    def __next__(self):
        if self.walk_node:
            nxt = self.walk_node
            self.walk_node = self.walk_node.next
            return nxt
        else:
            raise StopIteration

    def __repr__(self):
        return f"""Linked list({len(self)})"""


class Node:
    def __init__(self, path: Path):
        self.path: Path = path
        self.next: Node = None
        self.disk_usage = self.__disk_usage()

    def __str__(self):
        return f"{'Folder' if self.path.is_dir() else 'File'}" + \
            f" Node : {self.path.absolute()}, {self.disk_usage}"

    def __disk_usage(self) -> str:
        def decode_size(bytesize: int) -> str:
            """переводим размер в байтах в читаемую строку"""
            out = ""
            mask = {0: "B",
                    1: "KB",
                    2: "MB",
                    3: "GB",
                    4: "TB"
                    }
            base = 1024
            pow_ = 0
            while base ** pow_ < bytesize:
                pow_ += 1

            for i in range(pow_, -1, -1):
                full_item = bytesize // base ** i
                if full_item:
                    bytesize = bytesize - full_item * (base ** i)
                    out += f"{full_item} {mask[i]},"
            out = out.strip(",")
            return out if out else "0 B"

        def get_size():
            try:
                if self.path.is_file():
                    return decode_size(getsize(self.path))
                out = 0
                for path, folders, files in os.walk(self.path):
                    for file in files:
                        out += getsize(Path.cwd()/path/file)
                return decode_size(out)
            except FileNotFoundError:
                return "File doesn't exist."

        return get_size()


def main(path_i: Path):
    a = LinkedList()
    for p, d, f in os.walk(path_i):
        for directory in d:
            a.append(Node(Path(directory)))
        for file in f:
            a.append(Node(Path(file)))
    b = iter(a)
    while True:
        try:
            print(next(b))
        except StopIteration:
            sys.exit(0)
if __name__ == '__main__':
    main(Path("."))
    # files = LinkedList()
    # a.append(Node(Path("a.txt")))
    # a.append(Node(Path("b.txt")))
    # a.append(Node(Path("t1.py")))
    # a.append(Node(Path(".")))
    # print(a)
    # b = iter(a)
    # while True:
    #     try:
    #         item: Node = next(b)
    #         print(item)
    #         print(item.disk_usage)
    #     except StopIteration:
    #         break
    # print("ok")
