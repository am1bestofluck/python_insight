from linked_list import LinkedList
from format import Format


class Extractor:
    def __init__(self, item):
        self.item: LinkedList = item
        self.structure = None

    def all_reports(self):
        self.structure = [itm.to_dict() for itm in list(iter(self.item))]
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
        for i in self.structure:
            print(i)
        print("jsonified")

    def __picklify(self):
        print("pickled")

    def __csvify(self):
        print("csvfied")
