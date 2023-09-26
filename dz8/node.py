import os
from os.path import getsize
from pathlib import Path


class Node:
    def __init__(self, path: Path):
        self.path: Path = path
        self.next: Node | None = None
        self.disk_usage = self.__disk_usage()

    def __str__(self):
        return f"{'Folder' if self.path.is_dir() else 'File'}" + \
            f" Node : {self.path.absolute()}, {self.disk_usage}"

    def __repr__(self):
        return str(self)

    def get_size(self):
        try:
            out = getsize(self.path) if self.path.is_file() else self.get_dir_size(self.path)
            return self.decode_size(out)
        except FileNotFoundError:
            return "File doesn't exist."

    def decode_size(self, bytesize: int) -> str:
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
        out = out.strip().strip(",")
        return out if out else "0 B"

    def get_dir_size(self, p: Path):
        """собираем из кусочков размер папки"""
        # честно украдено у интернета :(
        total = 0
        with os.scandir(p) as d:
            for f in d:
                if f.is_file():
                    total += f.stat().st_size
                elif f.is_dir():
                    total += self.get_dir_size(f.path)
        return total

    def __disk_usage(self) -> str:
        return self.get_size()

    def to_dict(self):
        return {"name": self.path, "size": self.disk_usage,
                "nature": "File" if self.path.is_file() else "Folder",
                "parent_folder":self.path.absolute().parts[-2]}
