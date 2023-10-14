"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import unittest

from sem14.t_2 import fAs_docked


class TestAllBullets(unittest.TestCase):
    ok = "ok"

    def test_no_edits(self):
        self.assertEqual(fAs_docked(self.ok), self.ok)

    def test_casetest(self):
        i = "OK"
        self.assertEqual(fAs_docked(i), self.ok)

    def test_rm_signs(self):
        i = ".,ok!?"
        self.assertEqual(fAs_docked(i), self.ok)

    def test_only_askii(self):
        i = "приветok"
        self.assertEqual(fAs_docked(i), self.ok)

    def test_stress_test(self):
        o = "   none shall survive"
        i = "звёзды пали во тьмуNONE SHALL SURVIVE!!!"
        self.assertEqual(fAs_docked(i), o)


if __name__ == '__main__':
    unittest.main()
