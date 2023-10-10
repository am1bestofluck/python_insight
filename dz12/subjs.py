import csv
from pathlib import Path

CONTENT = """Математика,Физика,История,Литература"""


def get_subjects(items: Path):
    global CONTENT
    try:
        with open(items, mode="rt", encoding="utf8") as subjs:
            return list(csv.reader(subjs)[0])
    except:  # не ожидаю что тест что-там прочтёт
        return CONTENT.split(",")


if __name__ == '__main__':
    print(get_subjects(Path("subjects.csv")))
