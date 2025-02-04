def gcd(a, b):

    while b != 0:
        t = b
        b = a % b
        a = t
    return abs(a)

class Frac:
    def __init__(self, numer, denom):
        self.numer = numer//gcd(numer, denom)
        self.denom = denom//gcd(numer, denom)

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def add(self, y):
        new_numer = (self.numer * y.denom) + (self.denom * y.numer)
        new_denom = self.denom * y.denom
        return Frac(new_numer, new_denom)

    def sub(self, y):
        new_numer = (self.numer * y.denom) - (self.denom * y.numer)
        new_denom = self.denom * y.denom
        return Frac(new_numer, new_denom)

    def mul(self, y):
        new_numer = self.numer * y.numer
        new_denom = self.denom * y.denom
        return Frac(new_numer, new_denom)

    def div(self, y):
        new_numer = self.numer * y.denom
        new_denom = self.denom * y.numer
        return Frac(new_numer, new_denom)
    def __add__(self, other):
        return Frac.add(self, y)
    def __sub__(self, other):
        return Frac.sub(self, y)
    def __mul__(self, other):
        return Frac.mul(self, y)
    def __truediv__(self, other):
        return Frac.div(self, y)

a = Frac(1, 3)
b = Frac(1, 3)
c = Frac(1, 6)
d = Frac(1, 6).mul(c).add(b).add(a)



x = Frac(1, 3)
y = Frac(1, 3)
result = x * y
print(result)
