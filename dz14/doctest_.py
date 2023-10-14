import doctest
from dz3.dz1 import testable as twins


def wrapper(ints: list[int]):
    """

    :param ints:  список чисел
    :return: уникальные числа ints, отсортированы

    >>> wrapper([3,3,2,1])
    [3]
    >>> wrapper([1,2,3,4,5,6,7,8,9,0])
    []
    >>> wrapper([7,8,8,7])
    [7,8]
    """
    return twins(ints)


if __name__ == '__main__':
    doctest.testmod()
