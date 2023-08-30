"""
Manual decimal-to-hex converter.
"""


def convert(i: int):
    prefix = "0x" if i > 0 else "-0x"

    return hex(i)


def test(i: int):
    for m in range(-i, i):
        assert hex(m) == convert(m)
    print('ok')


if __name__ == '__main__':
    test(100)
