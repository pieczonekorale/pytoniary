from Point import Point
import math

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)
        if ((self.p2.x - self.p1.x) * (self.p3.y - self.p1.y) - (self.p2.y - self.p1.y) * (self.p3.x - self.p1.x)) == 0:
            raise ValueError("nie da się zbudować trójkąta")

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"

        return '['+'{self.p1},{self.p2},{self.p3}'.format(self=self)+']'
    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return 'Triangle('+'{self.p1.x}, {self.p1.y}, {self.p2.x}, {self.p2.y}, {self.p3.x}, {self.p3.y}'.format(self=self)+')'

    def __eq__(self, other):  # obsługa tr1 == tr2
        return self.p1==other.p1 and self.p2==other.p2 and self.p3==other.p3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        return Point((self.p1.x+self.p2.x+self.p3.x)/3, (self.p1.y+self.p2.y+self.p3.y)/3)

    def area(self):             # pole powierzchni
        field=0.5*math.fabs((self.p2.x-self.p1.x)*(self.p3.y-self.p1.y)-(self.p2.y-self.p1.y)*(self.p3.x-self.p1.x))
        return field

    def move(self, x, y):       # przesunięcie o (x, y)
        move_vec=Point(x,y)
        pt1=self.p1+move_vec
        pt2=self.p2+move_vec
        pt3=self.p3+move_vec
        temp = Triangle(pt1.x, pt1.y, pt2.x, pt2.y, pt3.x, pt3.y)
        return temp
