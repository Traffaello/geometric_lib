import math


def area(r):
    """Функция вычисляет значение площади круга с радиусом r"""
    if r < 0:
        raise ValueError("Negative number in radius")
    return math.pi * r * r


def perimeter(r):
    """Функция вычисляет значение периметра круга с радиусом r"""
    if r < 0:
        raise ValueError("Negative number in radius")
    return 2 * math.pi * r
