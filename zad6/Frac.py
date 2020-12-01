class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if self.y == 0:
            self.y = 1

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y==1:
            return '{self.x}'.format(self=self)
        else:
            return '{self.x}'.format(self=self)+'/'+'{self.y}'.format(self=self)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return 'Frac(' + '{self.x}, {self.y}'.format(self=self) + ')'


    def skracanie(self):
        a = self.x
        b = self.y
        while a != b:
            a, b = max(a, b), min(a, b)
            a = a - b
        self.x = int(self.x/a)
        self.y = int(self.y/a)

    def denominator(self, other): #szukanie wspolnego mianownika
        a = self.y
        b= other.y
        dn = 1
        while a != b:
            a, b = max(a, b), min(a, b)
            a = a - b

        dn=int(self.y/a*other.y)
        return dn

    def comm(self, dn): #update mianownika
        if self.y != dn:
            old_y = self.y
            self.y=dn
            self.x=int(self.x*(dn/old_y))

    def cd(self, other): #obsluga sprowadzania do wspolnego mianownika
        if self.y != other.y:
            dn = self.denominator(other)
            self.comm(dn)
            other.comm(dn)

    # metody cd
    def __eq__(self, other):
        self.cd(other)
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):
        self.cd(other)
        return not self.x == other.x and self.y == other.y

    def __lt__(self, other):
        self.cd(other)
        return self.x < other.x

    def __le__(self, other):
        self.cd(other)
        return self.x <= other.x

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):  # frac1 + frac2
        self.cd(other)
        fr = Frac(1,1)
        fr.x=self.x+other.x
        fr.y=self.y
        fr.skracanie()
        return fr

    def __sub__(self, other):   # frac1 - frac2
        self.cd(other)
        fr = Frac(1, 1)
        fr.x = self.x - other.x
        fr.y = self.y
        fr.skracanie()
        return fr

    def __mul__(self, other):  # frac1 * frac2
        fr = Frac(1, 1)
        self.cd(other)
        fr.x = self.x * other.x
        fr.y = self.y * other.y
        fr.skracanie()
        return fr

    def __div__(self, other):
        fr = Frac(1, 1)
        self.cd(other)
        fr.x = self.x * other.y
        fr.y = self.y * other.x
        fr.skracanie()
        return fr

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        fr = Frac(1, 1)
        self.cd(other)
        fr.x = self.x * other.y
        fr.y = self.y * other.x
        fr.skracanie()
        return fr

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        a = self.x / self.y
        b = other.x / other.y
        return a // b

    def __mod__(self, other):   # frac1 % frac2, opcjonalnie
        a = self.x/self.y
        b=other.x/other.y
        return a % b


    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self): pass       # float(frac)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

