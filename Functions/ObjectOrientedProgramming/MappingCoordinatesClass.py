class Coordinate(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        #Represetation of an object
        return "<"+str(self.x) + ","+ str(self.y)+">"
    
    
c = Coordinate(3,4)
zero = Coordinate(0, 0)
"""Using the class
   conventional way call by object"""
# print(c.distance(zero))

"""Using the class
   equivalent to call by name of class"""

print(Coordinate.distance(c, zero))

"""Print representation of an object"""
print(c)
print(type(c))
print(type(Coordinate))
print(isinstance(c, Coordinate))

# print(c.__add__(zero))
# print(c.__sub__(zero))
# print(c.__eq__(zero))
# print(c.__lt__(zero))
# print(c.__len__(c))

