"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json
from pathlib import Path

from sem12.t_1 import FactorialOf


class FactorialWriter(FactorialOf):
    def __init__(self, k: int, file_path: Path):
        self._filePath = file_path
        super().__init__(k)

    def __enter__(self):
        self._file = open(self._filePath, 'wt')
        return  self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        tmp = json.dumps(self.get_vals(),indent=1)
        self._file.write(tmp)
        self._file.close()

if __name__ == '__main__':
    with FactorialWriter(100,Path("t2_out.json")) as base:
        print("ok")

