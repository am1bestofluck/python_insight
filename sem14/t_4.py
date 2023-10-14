"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import pytest

OK = "ok"
FAIL = "redo"

from sem14.t_3 import fAs_docked


def test_no_edit():
    assert fAs_docked(OK) == OK, FAIL


def test_case_edit():
    assert fAs_docked(OK.upper()) == OK, FAIL


def test_rm_signs():
    assert fAs_docked(OK + ",.!?") == OK, FAIL


def test_only_ASKII():
    assert fAs_docked(f"привет{OK}какдела") == OK, FAIL

def test_stress_test():
    assert fAs_docked(f"йцфвуыаппиаууцкпаoh12325436523!!!!/,/.,/.,/,/ {OK}") == "oh ok", FAIL
if __name__ == '__main__':
    pytest.main()
