from calculate import calc
import unittest
import math


class TestCalculate(unittest.TestCase):
    def test_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        res = calc(fig, func, size)
        self.assertEqual(res, 25 * math.pi)

    def test_square_area(self):
        fig = "square"
        func = "area"
        size = [5]
        res = calc(fig, func, size)
        self.assertEqual(res, 25)

    def test_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [5, 4]
        res = calc(fig, func, size)
        self.assertEqual(res, 10)

    def test_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [5]
        res = calc(fig, func, size)
        self.assertEqual(res, 10 * math.pi)

    def test_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [5]
        res = calc(fig, func, size)
        self.assertEqual(res, 20)

    def test_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [5, 7, 3]
        res = calc(fig, func, size)
        self.assertEqual(res, 15)

    def test_wrong_fig(self):
        fig = "rectangle"
        func = "area"
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_func(self):
        fig = "Circle"
        func = "diagonal"
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_size(self):
        fig = "square"
        func = "area"
        size = [5, 4]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_circle(self):
        fig = "circle"
        func = "area"
        size = [-5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_square(self):
        fig = "square"
        func = "area"
        size = [-5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_triangle(self):
        fig = "triangle"
        func = "perimetr"
        size = [-5, -7, -4]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_size_triangle(self):
        fig = "triangle"
        func = "perimetr"
        size = [1, 2, 10]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
