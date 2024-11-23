def area(a):
    """Функция вычисляет площадь квадрата со стороной a"""
    if a < 0:
        raise ValueError("Negative number in side")
    return a * a


def perimeter(a):
    """Функция вычисляет периметр квадрата со стороной a"""
    if a < 0:
        raise ValueError("Negative number in side")
    return 4 * a
