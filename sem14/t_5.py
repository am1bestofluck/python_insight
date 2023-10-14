"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""

import unittest

from sem12_m.t_6 import RectangleWithDescriptors


class TestRectangle(unittest.TestCase):
    fail = "redo"

    def setUp(self) -> None:
        self.unit_ = RectangleWithDescriptors(3, 4)
        self.other = RectangleWithDescriptors(3, 4)

    def test1(self):
        self.assertEqual(self.unit_.w, 3, self.fail)

    def test2(self):
        self.assertEqual(self.unit_.h, 4, self.fail)

    def test3(self):
        self.assertEqual(str(self.unit_), f"Rectangle {self.unit_.w}x{self.unit_.h}", self.fail)

    def test4(self):
        self.assertEqual(self.unit_.per(), 14, self.fail)

    def test5(self):
        self.assertEqual(self.unit_.sq(), 12, self.fail)

    def test6(self):
        self.assertTrue(self.unit_ == self.other)

    def test7(self):
        with self.assertRaises(expected_exception=ValueError):
            self.unit_.w = -1


if __name__ == '__main__':
    unittest.main()
