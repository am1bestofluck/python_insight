import json
import csv
from pathlib import Path
import pickle

from linked_list import LinkedList
from format import Format


class Extractor:
    def __init__(self, item:LinkedList,output_folder:Path):
        self.item: LinkedList = item
        self.structure = [itm.to_dict() for itm in list(iter(self.item))]
        self.output_folder = output_folder/"extracted"
    def all_reports(self):
        for i in [Format.csv_ed, Format.json_ed, Format.pickle_ed]:
            self.convert(i)

    def convert(self, sign: Format):
        match sign.value:
            case 1:
                self.__jsonify()
            case 2:
                self.__csvify()
            case 3:
                self.__picklify()
            case _:
                raise ValueError("Кто ты?")

    def __jsonify(self):
        with open(file=f"{self.output_folder}.json", mode="w", encoding="utf-8") as core:
            tmp = json.dumps(self.structure,indent=1)
            core.write(tmp)
        return

    def __picklify(self):
        print("pickled")

    def __csvify(self):
        print("csvfied")
