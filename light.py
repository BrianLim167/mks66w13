from vector import *

class Light(object):

    def __init__( self, location, color ):
        self.location = location
        self.color = color

    @staticmethod
    def ambient_color( ambient_light, reflection ):
        return [ ambient_light[0]*reflection[0],
                 ambient_light[1]*reflection[1],
                 ambient_light[2]*reflection[2] ]

    def diffuse_color( self, reflection, normal ):
        normal_mul = Vector.dot(self.location, normal)
        if ( normal_mul < 0 ):
            normal_mul = 0
        return [ int(self.color[0] * reflection[0] * normal_mul),
                 int(self.color[1] * reflection[1] * normal_mul),
                 int(self.color[2] * reflection[2] * normal_mul) ]

    def specular_color( self, reflection, view, normal, specular_exp=8 ):
        normal_mul = 2 * Vector.dot(self.location, normal)
        v = Vector([ (normal[0] * normal_mul) - self.location[0],
                     (normal[1] * normal_mul) - self.location[1],
                     (normal[2] * normal_mul) - self.location[2] ])
        view_mul = Vector.dot(v, view)
        if ( view_mul < 0 ):
            view_mul = 0
        view_mul = view_mul ** specular_exp
        return [ int(self.color[0] * reflection[0] * view_mul),
                 int(self.color[1] * reflection[1] * view_mul),
                 int(self.color[2] * reflection[2] * view_mul) ]
