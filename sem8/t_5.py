"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов
"""
import json
import os
from pathlib import Path
import pickle


def read_json(path_i: Path):
    with open(path_i) as content:
        return json.loads("".join(content.readlines()), parse_int=int)


def pickle_ize(path_o: Path, content: dict):
    with open(path_o, "wb") as file_o:
        pickle.dump(content, file_o)


def walk_dir(target_dir: Path, new_name: Path = None) -> None:
    for path, folder, files in os.walk(target_dir):
        for file in files:
            if Path(file).suffix != ".json":
                continue
            temp = read_json(Path(file).absolute())
            new_name = Path(f"{Path(file).stem}.pickle")
            pickle_ize(new_name, temp)


if __name__ == '__main__':
    walk_dir(Path("."))
