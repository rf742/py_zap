#!/usr/bin/env python3

import math

K = 8.988E9 #Coulombs constant
e = -1.602217662E-19 # charge on electron
class pointCharge():
    def __init__(self, x,y,q):
        self.x = x
        self.y = y
        self.q = q
        self.fx = 0
        self.fy = 0
        self.magf = 0
        self.netangle = 0

def main():
    bob = [pointCharge(0,2E-7,2*e), pointCharge(0,0,-3*e), pointCharge(4E-7,0,-5*e)]
    for i, point in enumerate(bob):
        for j, p in enumerate(bob):
            if i != j:
                x_dist = (p.x - point.x)
                y_dist = (p.y - point.y)
                dist = ((x_dist**2)+(y_dist**2))**.5
                totalforce = (K*point.q * p.q)/(dist**2)
                angle = math.atan2(y_dist,x_dist)
                bob[i].fx += totalforce*math.cos(angle)
                bob[i].fy += totalforce*math.sin(angle)
    for p in bob:
        p.magf = math.sqrt(p.fx**2 + p.fy**2)
        p.netangle = math.atan2(p.fy,p.fx)
        print(f'The {p.q} C charge @ {p.x},{p.y}')
        print(f'experiences a force of total magnitude {abs(p.magf)} N\n')
        print(f'This force occurs at an angle of {p.netangle} radians')
        print(f'                                 {p.netangle*180/math.pi} degrees')

if __name__ == "__main__":
    main()
