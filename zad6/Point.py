import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): # zwraca string "(x, y)"
        return '('+'{self.x}, {self.y}'.format(self=self)+')'

    def __repr__(self):        # zwraca string "Point(x, y)"
        return 'Point(' + '{self.x}, {self.y}'.format(self=self) + ')'

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x==other.x and self.y==other.y
        #return self==other

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        p1= Point(1,1)
        p1.x=self.x+other.x
        p1.y=self.y+other.y
        return p1

    def __sub__(self, other):  # v1 - v2
        p1 = Point(1, 1)
        p1.x = self.x - other.x
        p1.y = self.y - other.y
        return p1

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return self.x*other.x+self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x


    def length(self):           # długość wektora
        return math.sqrt(pow(0-self.y, 2)+pow(0-self.x, 2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

