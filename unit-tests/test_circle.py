import unittest
import math
import sys
from circle import area, perimeter

sys.path.append("..")


class TestCaseCircle(unittest.TestCase):
    def perimetr_standart_1(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def perimetr_standart_2(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def perimetr_standart_3(self):
        self.assertEqual(perimetr(0), 0)

    def area_standart_1(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)

    def area_standart_2(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def area_standart_3(self):
        self.assertEqual(area(0), 0)

    def perimetr_invalid(self):
        with self.assertRaises(TypeError):
            perimeter("five")
        with self.assertRaises(ValueError):
            perimeter(-5)

    def area_invalid(self):
        with self.assertRaises(TypeError):
            area("five")
        with self.assertRaises(ValueError):
            area(-5)


if _name_ == "_main_":
    unittest.main()
