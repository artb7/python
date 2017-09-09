#! /home/jbjeong/.conda/envs/myenv/bin/python

from math import hypot 

class Vector():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #return 'Vector(%r, %r)' % (self.x, self.y)
        return 'Vector({0!r}, {1!r})'.format(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        #return math.sqrt(self.x*self.x + self.y*self.y)
        return hypot(self.x, self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))
print(v * 3)
print(abs(v * 3))

if v:
    print('yes')
    print(v)
