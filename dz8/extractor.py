import json
import csv
from pathlib import Path
import pickle

try:
    from linked_list import LinkedList
    from format import Format
except ImportError:
    from .linked_list import LinkedList
    from .format import Format

class Extractor:
    def __init__(self, item: LinkedList, output_folder: Path):
        self.item: LinkedList = item
        self.structure = [itm.to_dict() for itm in list(iter(self.item))]
        self.output_folder = output_folder / "extracted"

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
            tmp = json.dumps(self.structure, indent=1)
            core.write(tmp)
        print("json-ified")
        return

    def __picklify(self):
        with open(file=f"{self.output_folder}.pickle", mode="bw") as core:
            pkl = pickle.dumps(bytes(str(self.structure), "utf-8"))
            core.write(pkl)
        print("pickle-ified")

    def __csvify(self):
        with open(file=f"{self.output_folder}.csv", mode="w", encoding="utf-8", newline="") as core:
            csv_write = csv.DictWriter(f=core, dialect="excel-tab", fieldnames=list(self.structure[0].keys()))

            csv_write.writeheader()
            for i in self.structure:
                csv_write.writerow(i)
        print("csv-ified...\n",
              "открывается в экселе в несколько колонок, всё красиво;",
              "но надо немного поплясать с бубном в самом экселе",
              "\nhttps://support.goteamup.com/faq-when-opening-.csv-file-all-data-appears-in-one-column")
