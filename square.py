
def area(a):
    ''' Функция вычисляет площадь квадрата со стороной a '''
    if a<0:
        raise ValueError("Negative number in side")
    if type (a)!=int:
        raise TypeError("Incorrect type of side")
    return a * a

def perimeter(a):
    ''' Функция вычисляет периметр квадрата со стороной a '''
    if a<0:
        raise ValueError("Negative number in side")
    if type (a)!=int:
        raise TypeError("Incorrect type of side")
    return 4 * a
