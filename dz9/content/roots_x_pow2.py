"""
https://skysmart.ru/articles/mathematic/kak-reshat-kvadratnye-uravneniya

"""
from math import sqrt


def roots(a: int, b: int, c: int) -> tuple[float] | tuple[float, float] | None:
    discr = 0

    def get_discr() -> None:
        """ну а чо, вся пара про это"""
        nonlocal a, b, c, discr
        discr = b ** 2 - 4 * a * c

    get_discr()
    if discr == 0:
        return -b / (2 * a),
    if discr > 0:
        try:
            return (
                (-b + sqrt(discr)) / (2 * a),
                (-b - sqrt(discr)) / (2 * a)
            )
        except ZeroDivisionError:
            return None # не получилось нарандомить квадратичное уравнение, да и ... так тоже хорошо
    return None


if __name__ == '__main__':
    print(roots(4, 4, 1))
    print(roots(1, 0, 1))
    print(roots(1, 10, 1))
