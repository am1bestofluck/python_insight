"""
Напишите функцию группового переименования файлов. Она должна:
*   принимать параметр желаемое конечное имя файлов.# new_name
#   При переименовании в конце имени добавляется порядковый номер.
*   принимать параметр количество цифр в порядковом номере. #number_size
*   принимать параметр расширение исходного файла.#target_ext
#   Переименование должно работать только для этих файлов внутри каталога. # ...ну ок; #краем уха слышал что-то о os_walk
*   принимать параметр расширение конечного файла.# new_ext
*   принимать диапазон сохраняемого оригинального имени. # saved_part
#        Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
        К ним прибавляется желаемое конечное имя, если оно передано.
        Далее счётчик файлов и расширение.
"""
import os
from pathlib import Path
from shutil import move


def main(
        folder_i: Path,  # методисты самое главное забыли, пф.
        *,
        target_ext: str, saved_part: range,
        new_name: str, number_size: int, new_ext: str):
    """переименовываем файлы..."""
    target_ext_m = "."+target_ext.lower()
    counter = 0
    for path_, folder_, file_ in os.walk(folder_i):
        for each_file in file_:
            if Path(each_file).suffix == target_ext_m:
                new_name_ = Path(
                    path_) / f"{new_name}_{Path(each_file).stem[saved_part.start:saved_part.stop]}({str(counter).zfill(number_size)}).{new_ext}"
                try:
                    move(
                        src = Path(path_) / each_file,
                        dst= new_name_)
                except FileNotFoundError:
                    print("?")
                counter += 1


if __name__ == '__main__':
    main(
        Path("./t6_f/t5"),
        target_ext="dll", saved_part=range(0, 4),
        new_name="renamed", number_size=4, new_ext="exe")
