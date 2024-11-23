def area(a, h):
    """Вычисляет значение площади треугольника со стороной a и высотой h"""
    if a < 0 or h < 0:
        raise ValueError("Negative number")
    return (a * h) / 2


def perimeter(a, b, c):
    """Вычисляет значение периметра треугольника со сторонами a, b, c"""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Negative number in radius")
    if a == 0 or b == 0 or c == 0:
        return 0
    if a + b < c or a + c < b or b + c < a:
        raise ValueError("Not a triangle")
    return a + b + c
