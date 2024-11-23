import unittest
import sys
from square import area, perimeter

sys.path.append("..")


class TestCaseSquare(unittest.TestCase):
    def perimeter_standart_1(self):
        self.assertEqual(perimeter(5), 20)

    def perimeter_standart_2(self):
        self.assertEqual(perimeter(2), 8)

    def perimeter_standart_3(self):
        self.assertEqual(perimeter(0), 0)

    def area_standart_1(self):
        self.assertEqual(area(5), 25)

    def area_standart_2(self):
        self.assertEqual(area(2), 4)

    def area_standart_3(self):
        self.assertEqual(area(0), 0)

    def perimeter_invalid(self):
        with self.assertRaises(TypeError):
            perimeter("five")
        with self.assertRaises(ValueError):
            perimeter(-5)

    def area_invalid(self):
        with self.assertRaises(TypeError):
            area("five")
        with self.assertRaises(ValueError):
            area(-5)


if __name__ == "__main__":
    unittest.main()
