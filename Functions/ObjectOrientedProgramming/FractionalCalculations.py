class Fraction(object):
    """
    A number represented as a fraction

    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    
    def __str__(self):
        """ Returns a string representation of self"""
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """ Returns a new fraction representing of addition"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __sub__(self, other):
        """ Returns a new fraction representing of subtraction"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ Retuns a float value of the fraction"""
        return self.num/self.denom

    def inverse(self):
        """ Returns a new fraction representing Inverse of the original fraction"""
        return Fraction(self.denom, self.num)






a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b
d = a - b
print(c)
print(d)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
