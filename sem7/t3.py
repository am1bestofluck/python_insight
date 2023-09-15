"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало
"""

from pathlib import Path

F1 = Path("t1_txt.txt")
F2 = Path("t2_txt.txt")
F3 = Path("t3_txt.txt")


def main():
    with(
        open(F1, "r") as f1,
        open(F2, "r") as f2,
        open(F3, "w") as f3
    ):
        lines_1 = list(f1.readlines())
        lines_2 = list(f2.readlines())
        for line_index in range(len(lines_1)):
            a = int(lines_1[line_index].split("|")[0])
            b = float(lines_1[line_index].split("|")[1])
            multiplied = a * b
            if multiplied >= 0:
                multiplied = round(multiplied, 0)
                name_ = lines_2[line_index].lower()
                pass
            else:
                multiplied = abs(multiplied)
                name_ = lines_2[line_index].upper()
                pass
            f3.write(f"{multiplied}|{name_}\n")
        pass


if __name__ == '__main__':
    main()
