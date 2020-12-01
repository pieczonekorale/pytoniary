import unittest
from Frac import Frac

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.fr1 = Frac(1,2)
        self.fr2 = Frac(2,4)
        self.fr3 = Frac(1,5)

    def test_str(self):
        self.assertEqual(str(self.fr1), '1/2')
        self.assertEqual(str(self.fr2), '2/4')
        self.assertEqual(str(self.fr3), '1/5')

    def test_repr(self):
        self.assertEqual(repr(self.fr1), 'Frac(1, 2)')
        self.assertEqual(repr(self.fr2), 'Frac(2, 4)')

    def test_eq(self):
        self.assertEqual(self.fr1, Frac(1,2))
        self.assertEqual(self.fr2, Frac(2,4))

    def test_ne(self):
        self.assertNotEqual(self.fr1, Frac(3,9))
        self.assertNotEqual(self.fr3, Frac(33,3))

    def test_lt(self):

        self.assertEqual(self.fr3 < self.fr1, True)
        self.assertEqual(self.fr3 < self.fr2, True)

    def test_le(self):
        self.assertEqual(self.fr3 <= self.fr1, True)
        self.assertEqual(self.fr1 <= self.fr2, True)

    def test_add(self):
        self.assertEqual(self.fr1+self.fr2, Frac(2, 2))
        self.assertEqual(self.fr1+self.fr3, Frac(7, 10))

    def test_sub(self):
        self.assertEqual(self.fr1-self.fr3, Frac(3,10))

    def test_mul(self):
       self.assertEqual(self.fr1*self.fr2, Frac(1,4))
       self.assertEqual(self.fr1*self.fr3, Frac(1, 10))

    def test_div(self):
        self.assertEqual(self.fr1 / self.fr2, Frac(1, 1))
        self.assertEqual(self.fr1 / self.fr3, Frac(5, 2))




if __name__ == "__main__":
    unittest.main()
