
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
В данной функции мы передаём радиус окружности, после чего она возвращает значение площади круга.
``` python
a = 5
ar = area(a)
```
Результатом работы функции будет значение 25 * pi.
- Rectangle: `S = ab`
В данной функции мы передаём длину и ширину прямоугольника, после чего она возвращает значение площади прямоугольника.
``` python
a = 5
b = 2
ar = area (a, b)
```
Результатом работы функции будет значение 10.
- Square: `S = a²`
В данной функции мы передаём длину стороны квадрата, после чего она возвращает значение площади квадрата.
``` python
a = 5
ar = area (a)
```
Результатом работы функции будет значение 25.
- Triangle: `S = (a + b + c) / 2`
В данной функции мы передаём три стороны треугольника, после чего она возвращает значение полупериметра треугольника.
``` python
a = 5
b = 2
c = 3
ar = area (a, b, c)
```
Результатом работы функции будет значение 5.
## Perimeter
- Circle: `P = 2πR`
В данной функции мы передаём радиус окружности, после чего она возвращает значение периметра круга.
``` python
a=5
per = perimetr (a) 
```
Результатом работы функции будет значение 10 * pi.
- Rectangle: `P = 2a + 2b`
В данной функции мы передаём длину и ширину прямоугольника, после чего она возвращает значение периметра прямоугольника.
```python
a=10
b=2
per = perimetr (a, b)
```
Результатом работы функции будет значение 24.
- Square: `P = 4a`
В данной функции мы передаём сторону квадрата, после чего она возвращает значение периметра квадрата.
``` python
a=5
per = perimetr (a)
```
Результатом работы функции будет значение 20.
- Triangle: `P = a + b + c`
В данной функции мы передаём три стороны треугольника, после чего она возвращает значение периметра треугольника.
``` python
a=5
b=2
c=3
per = perimetr (a, b, c)
```
Результатом работы функции будет значение 10.

# Commits
## L-03
- Circle and square added
- Docs added
- Docs added
## L-04
- Triangle added
- Doc updated for triangle
- Add calculate.py
- Update docs for calculate.py
- Add rectangle.py
## L-05
- Add user agreement
- Update docs. Add user agreement info