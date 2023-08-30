"""
Manual decimal-to-hex converter.
"""


def convert(i: int):
    result = ""
    div = abs(i)
    if div == 0:
        return "0x0" # если это неок - переделаю
    while div > 0:
        div, mod = divmod(div, 16)
        match mod:
            case 10:
                mod = "a"
            case 11:
                mod = "b"
            case 12:
                mod = "c"
            case 13:
                mod = "d"
            case 14:
                mod = "e"
            case 15:
                mod = "f"
            case _:
                mod = str(mod)
        result = mod+result
    return f"{'' if i >= 0 else '-'}0x{result}"


def test(i: int):
    for m in range(-i, i):
        assert hex(m) == convert(m)
    print('ok')


if __name__ == '__main__':
    test(100000)
