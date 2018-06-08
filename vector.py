import math

class Vector(object):

    def __init__(self, ary):
        self.ary = ary

    def copy(self):
        v = Vector([])
        for i in range( len(self) ):
            v.append(self[i])
        return v
        
    def __mul__(self, other):
        v = self.copy()
        for i in range( len(self) ):
            v[i] *= other
        return v

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self = self * other
        return self

    def __neg__(self):
        return -1 * self

    def __add__(self, other):
        v = self.copy()
        for i in range( len(self) ):
            v[i] += other[i]
        return v

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        v = self.copy()
        for i in range( len(self) ):
            v[i] -= other[i]
        return v

    def __isub__(self, other):
        self = self - other
        return self

    def __len__(self):
        return len(self.ary)

    def __getitem__(self, i):
        return self.ary[i]

    def __setitem__(self, i, val):
        self.ary[i] = val
        return self.ary[i]

    def append(self, val):
        self.ary.append(val)

    def norm(self):
        v = Vector([])
        square_sum = 0
        for i in range(len(self)):
            square_sum += self[i] ** 2
        for i in range(len(self)):
            v.append( self[i] / (square_sum ** 0.5) )
        return v

    @staticmethod
    def cross(v0, v1):
        v = Vector([])
        v.append(v0[1]*v1[2] - v0[2]*v1[1])
        v.append(v0[2]*v1[0] - v0[0]*v1[2])
        v.append(v0[0]*v1[1] - v0[1]*v1[0])
        return v

    @staticmethod
    def dot(v0, v1):
        ans = 0
        for i in range(len(v0)):
            ans += v0[i] * v1[i]
        return ans

    @staticmethod
    def normal(p0, p1, p2):
        edge0 = Vector(p1) - Vector(p0)
        edge1 = Vector(p2) - Vector(p0)
        return Vector.cross(edge0,edge1)
