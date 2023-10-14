"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

from sem14.t_1 import filter_ASKII_spaces


def fAs_docked(text: str):
    """
    >>> fAs_docked("no tweaks")
    'no tweaks'
    >>> fAs_docked("CASEswap")
    'caseswap'
    >>> fAs_docked(".,!strip symbols?:))")
    'strip symbols'
    >>> fAs_docked("Dust fights the windПрахкпраху")
    'dust fights the wind'
    >>> fAs_docked("Main reason for testing,,, is making sure nothing goes кривоwrong")
    'main reason for testing is making sure nothing goes wrong'
    """
    return filter_ASKII_spaces(text)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)