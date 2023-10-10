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

from dz12.subjs import get_subjects
from dz12.Descriptor import TitleCaseASKII


class Student:
    def __init__(self, name, subjects_file):
        raise NotImplemented

    def add_subject(self, subject, grade, test_score):
        raise NotImplemented

    def get_average_grade(self):
        raise NotImplemented

    @staticmethod
    def get_average_grades(students: list['Student']):
        def calc_average(one: Student):
            raise NotImplemented

        for i in students:
            calc_average(i)
        raise NotImplemented  # зачем это в классе студент на.за.чем.

    @staticmethod
    def get_top_student(students, subject):
        raise NotImplemented  # туда же. Что бы что. Зачем ячейке студент знать аналитику потока.
