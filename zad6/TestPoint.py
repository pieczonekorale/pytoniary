import math
import unittest
from Point import Point

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1=Point(1,1)
        self.p2=Point(5,10)
        self.p3=Point(2,4)
        self.p4=Point(1,3)

    def test_str(self):
        self.assertEqual(str(self.p1), '(1, 1)')
        self.assertEqual(str(self.p2), '(5, 10)')

    def test_repr(self):
        self.assertEqual(repr(self.p1), 'Point(1, 1)')
        self.assertEqual(repr(self.p3), 'Point(2, 4)')
        self.assertEqual(repr(self.p4), 'Point(1, 3)')

    def test_eq(self):
        self.assertEqual(self.p2, self.p2)
        self.assertEqual(self.p3, self.p3)

    def test_ne(self):
        self.assertNotEqual(self.p1, self.p3)
        self.assertNotEqual(self.p2, self.p4)

    def test_add(self):
        self.assertEqual(self.p1 + self.p3, Point(3,5))
        self.assertEqual(self.p1 + self.p2, Point(6, 11))
        self.assertEqual(self.p4 + self.p3, Point(3, 7))

    def test_sub(self):
        self.assertEqual(self.p2 - self.p3, Point(3, 6))
        self.assertEqual(self.p1 - self.p2, Point(-4, -9))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 15)
        self.assertEqual(self.p3 * self.p4, 14)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 5)
        self.assertEqual(self.p3.cross(self.p4), 2)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(2))
        self.assertEqual(self.p2.length(), math.sqrt(125))
        self.assertEqual(self.p3.length(), math.sqrt(20))
        self.assertEqual(self.p4.length(), math.sqrt(10))


if __name__ == "__main__":
    unittest.main()
