import math
from Point import Point

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"

        return '('+'{self.pt.x}, {self.pt.y}, {self.radius}'.format(self=self) + ')'

    def __repr__(self):        # "Circle(x, y, radius)"
        return 'Circle(' + '{self.pt.x}, {self.pt.y}, {self.radius}'.format(self=self) + ')'

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return 2*math.pi*self.radius

    def move(self, x, y):    # przesuniecie o (x, y)
        wheel=Circle(self.pt.x+x,self.pt.y+y,self.radius)
        return wheel

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        back1=Point(self.pt.x-self.radius, self.pt.y)
        print(back1)
        front1=Point(self.pt.x+self.radius, self.pt.y)
        print(front1)

        back2= Point(other.pt.x-other.radius, other.pt.y)
        front2 = Point(other.pt.x + other.radius, other.pt.y)
        print(back2)
        print(front2)

        if back1.x<back2.x:
            back=back1
        else:
            back = back2

        print(back)
        if front1.x>front2.x:
            front=front1
        else:
            front=front2
        print(front)

        big_radius=(back.vec_length(front)/2)
        center=Point(back.x+front.x/2, back.y+front.y/2)

        big=Circle(back.x+front.x/2, back.y+front.y/2, 4)
        return big