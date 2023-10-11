from random import randint
import csv
from pathlib import Path

from dz12.subjs import get_subjects


class ReportWriter:
    def __init__(self, path: Path, items_count: int):
        self.path = path
        self._content = ""
        self.items_count = items_count

    def __enter__(self):
        self._file = open(self.path, mode="wt", encoding="utf-8")
        self._content = csv.DictWriter(fieldnames=get_subjects(), f=self._file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.generate()

        pass

    def generate(self):
        a = randint(0, self.items_count)
        self._add_tests(self.items_count-a)
        self._add_grades(a)

    @staticmethod
    def _add_tests(qua: int):
        pass

    @staticmethod
    def _add_grades(qua: int):
        pass


if __name__ == '__main__':
    with ReportWriter(Path("grades_Ivanov.csv"), 15) as f:
        f.generate()

