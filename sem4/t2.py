"""
Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию
"""


def main():
    # надеюсь что микрофон работает...гуглю как получить юникод-код символа
    letters = list(__doc__)
    out = []
    for letter in letters:
        out.append(ord(letter))
    out = list(set(out))
    out.sort(reverse=True)
    return out


if __name__ == '__main__':
    print(main())
    # assert len(main()) == len(__doc__)
