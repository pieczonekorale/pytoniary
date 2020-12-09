import math
import unittest
from Point import Point
from Circle import Circle

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.cr1=Circle(2,2,1)
        self.cr2=Circle(7,3,2)

    def test_str(self):
        self.assertEqual(str(self.cr1), '(2, 2, 1)')

    def test_repr(self):
        self.assertEqual(repr(self.cr1), 'Circle(2, 2, 1)')

    def test_eq(self):
        self.assertEqual(self.cr1, Circle(2,2,1))

    def test_ne(self):
        self.assertNotEqual(self.cr1, Circle(2,4,3))

    def test_area(self):
        self.assertEqual(self.cr1.area(), 2*math.pi)
        self.assertEqual(self.cr2.area(), 2*math.pi*2)

    def test_move(self):
        self.assertEqual(self.cr1.move(3,-4), Circle(5,-2,1))

    def test_cover(self):
        self.assertEqual(self.cr1.cover(self.cr2), Circle(5, 2.5, 4))


if __name__ == "__main__":
    unittest.main()
