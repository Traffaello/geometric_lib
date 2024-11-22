import unittest
import sys
from triangle import area, perimetr

sys.path.append("..")


class TestCaseTriangle(unittest.TestCase):
    def perimetr_standart_1(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def perimetr_standart_2(self):
        self.assertEqual(perimeter(0, 5, 5), 0)

    def perimetr_standart_3(self):
        self.assertEqual(perimetr(5, 0, 5), 0)

    def perimetr_standart_3(self):
        self.assertEqual(perimetr(5, 5, 0), 0)

    def area_standart_1(self):
        self.assertEqual(area(5, 4), 10)

    def area_standart_2(self):
        self.assertEqual(area(2, 0), 0)

    def area_standart_3(self):
        self.assertEqual(area(0, 5), 0)

    def perimetr_invalid(self):
        with self.assertRaises(TypeError):
            perimeter("five", "five", "five")
        with self.assertRaises(ValueError):
            perimeter(-5, 5, 5)
        with self.assertRaises(ValueError):
            perimeter(5, -5, 5)
        with self.assertRaises(ValueError):
            perimeter(5, 5, -5)
        with self.assertRaises(ValueError):
            perimeter(3, 5, 8)

    def area_invalid(self):
        with self.assertRaises(TypeError):
            area("five", "five")
        with self.assertRaises(ValueError):
            area(-5, 5)
        with self.assertRaises(ValueError):
            perimeter(5, -5)


if _name_ == "_main_":
    unittest.main()
