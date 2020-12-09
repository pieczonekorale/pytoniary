import math
import unittest
from Point import Point
from Triangle import Triangle

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.tr1=Triangle(0,5,5,0,0,0)
        #self.tr2=Triangle(2,5,2,2,2,9)

    def test_str(self):
        self.assertEqual(str(self.tr1), '[(0, 5),(5, 0),(0, 0)]')

    def test_eq(self):
        self.assertEqual(self.tr1, Triangle(0,5,5,0,0,0))

    def test_ne(self):
        self.assertNotEqual(self.tr1, Triangle(2,3,1,7,6,7))

    def test_repr(self):
        self.assertEqual(repr(self.tr1), 'Triangle(0, 5, 5, 0, 0, 0)')

    def test_center(self):
        self.assertEqual(self.tr1.center(), Point(5/3, 5/3))

    def test_area(self):
        self.assertEqual(self.tr1.area(), 12.5)

    def test_move(self):
        self.assertEqual(self.tr1.move(2,4), Triangle(2,9,7,4,2,4))



if __name__ == "__main__":
    unittest.main()
