import math


class pointCharge():
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
        self.fx = 0
        self.fy = 0
        self.magf = 0
        self.netangle = 0
# method returns a list [resultant, angle]
# optional arg degrees, if True, give angle in degrees, rather than radians]
    def resolve(self, degrees = False):
        out = [math.hypot(self.fx,self.fy), math.atan2(self.fy,self.fx) if not degrees else math.atan2(self.fy,self.fx)*180/math.pi]
        return out
    def get_components(self,):
        return[self.fx,self.fy]
