"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие
только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
 и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл
записана следующая информация.

Математика,Физика,История,Литература


Создайте класс Student, который будет представлять студента и его успехи
 по предметам. Класс должен иметь следующие методы:

__init__(self, name, subjects_file): конструктор класса,
принимающий ФИО студента и имя файла с данными о предметах и оценках.

add_subject(self, subject, grade, test_score): метод для
добавления информации о предмете, оценке и результате теста.

get_average_grade(self): метод, возвращающий средний
балл студента по всем предметам.

get_subjects(self): метод, возвращающий список всех предметов
, по которым есть информация у студента.

Реализовать функцию get_average_grades(students), которая принимает
список студентов и выводит информацию о средних баллах для каждого студента.

Реализовать функцию get_subject_average(students, subject), которая
принимает список студентов и название предмета, и выводит информацию о среднем
балле по этому предмету для каждого студента.

Реализовать функцию get_top_student(students, subject), которая принимает
 список студентов и название предмета, и выводит информацию о студенте
  с наивысшим средним баллом по этому предмету.
"""
from copy import deepcopy
import csv
from string import digits
from dz12.subjs import get_subjects
from dz12.Descriptor import TitleCaseASKII
from pathlib import Path


class Student:
    name = TitleCaseASKII(ban=digits)
    grade_limit = range(2, 5+1)
    test_limit = range(0, 100+1)

    def __init__(self, name, subjects_file):
        self.name = name
        self._path = subjects_file
        self.subjects = get_subjects(subjects_file)

    def add_subject(self, subject, grade=None, test_score=None):
        temp = {i: '' for i in self.subjects}
        if grade and test_score:
            raise SyntaxError("either grade or test")
        if subject not in self.subjects:
            raise NotImplemented("Unsupported subject")
        if grade:
            assert grade in self.grade_limit
            temp[subject] = f"{grade=}"
        if test_score:
            assert test_score in self.test_limit
            temp[subject] = f"{test_score=}"

        b4 = self._prev_notes
        b4.append(temp)
        self._write_notes(b4)

    @property
    def _prev_notes(self):
        with open(self._path, mode="rt", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def _write_notes(self, new: list[dict]):
        with open(file=self._path, mode="wt", encoding="utf-8") as file:
            a = csv.DictWriter(file, fieldnames=self.subjects, dialect="excel")
            a.writeheader()
            a.writerows(new)

    def get_average_grade(self):
        b4 = self._prev_notes
        out = dict()
        for k_ in b4[0]:
            out[k_] = [{"grades": [], "tests": []}, 0, 0]
        for i in b4:
            for k_ in out:
                if i[k_]:
                    if i[k_].startswith("grade"):
                        out[k_][0]["grades"].append(int(i[k_].split("=")[1]))
                        out[k_][1] += 1
                        continue
                    out[k_][0]["tests"].append(int(i[k_].split("=")[1]))
                    out[k_][2] += 1
        tmp = {}
        for o_ in out:

            for val in ["grades", 1], ["tests", 2]:
                try:
                    tmp[val[0]] = round(sum(out[o_][0][val[0]]) / out[o_][val[1]], 2)
                except ZeroDivisionError:
                    tmp[val[0]] = None
            out[o_] = deepcopy(tmp)

        return out

    def get_subjects(self):
        b4 = self._prev_notes
        out = set()
        items = list(b4[0].keys())
        for i in b4:
            for j in items:
                if i[j] != '':
                    out.add(j)
                    items.remove(j)
        return out

    @staticmethod
    def get_average_grades(*args: 'Student'):
        out = {}
        for std in args:
            out[std.name] = std.get_average_grade()
        return out

    @staticmethod
    def get_subject_average(students, subject):
        raise NotImplemented

if __name__ == '__main__':
    a = Student(name="Asd Qwe", subjects_file=Path("subjects.csv"))
    a.add_subject("Литература", grade=3)
    a.add_subject("История", test_score=56)
    a.get_average_grade()
    a.get_subjects()
    b = Student(name="Asd Qasd", subjects_file=Path("subjects2.csv"))
    Student.get_average_grades(a, b)
