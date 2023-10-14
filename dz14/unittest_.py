import unittest

from dz2.fractions_calc import FractionsCalc


class TestFractions(unittest.TestCase):

    def setUp(self) -> None:
        print("1")
        self.main = FractionsCalc("1/1+1/1")

    def test_sum(self):
        self.main.get_next("3/3+8/8")
        self.assertEqual(self.main.eval(), "2/1")

    def test_sub(self):
        self.main.get_next("3/3-8/8")
        self.assertEqual(self.main.eval(), "0/24")  # мде :)
        # оно конечно, математически, всё равно правильно.
        # Но если бы мне нужно было подогнать своё решение под такой тест
        # Я бы ... очень недоволен был сложившейся ситуацией  XDDDDD

    def test_mult(self):
        self.main.get_next("2/5*5/4")
        self.assertEqual(self.main.eval(), "1/2")

    def test_div(self):
        self.main.get_next("2/5/5/4")
        self.assertEqual(self.main.eval(), "8/25")


if __name__ == '__main__':
    unittest.main()
