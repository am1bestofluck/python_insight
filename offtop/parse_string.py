import csv

HEADER = ["Продукт", "Калорийность, кКал", "Белки, г", "Жиры, г", "Углеводы, г"]


def to_dict(line: str):
    h = HEADER
    line = line.replace(",", ".").split("\t")
    return {h[0]: line[0],
            h[1]: round(float(line[1].strip("кКал")), 2),
            h[2]: round(float(line[2].strip("г")), 2),
            h[3]: round(float(line[3].strip("г")), 2),
            h[4]: round(float(line[4].strip("г\n")), 2)}


def main():
    with (open(file="raw.txt", mode="rt", encoding="utf-8") as core,
          open(file="out.csv", mode="wt", encoding="utf-8") as out):
        content = core.readlines()
        writer = csv.DictWriter(f=out,
                                fieldnames=HEADER,
                                dialect="excel-tab")
        writer.writeheader()
        writer.writerows([to_dict(line) for line in content])


if __name__ == '__main__':
    main()
