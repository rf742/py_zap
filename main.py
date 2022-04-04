#!/usr/bin/env python3

import math

K = 8.988E9 # Coulomb constant
e = -1.602217662E-19 # charge on electron

class pointCharge():
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
        self.fx = 0
        self.fy = 0
        self.magf = 0
        self.netangle = 0

def main():
    charges = [pointCharge(0,4,-6E-6), pointCharge(0,0,4E-6), pointCharge(3,0,2E-6)]
#   see https://farside.ph.utexas.edu/teaching/316/lectures/node20.html

    for i, p1 in enumerate(charges):
        for j, p2 in enumerate(charges):
            if i != j:
                x_dist = (p2.x - p1.x)
                y_dist = (p2.y - p1.y)
                dist = math.sqrt((x_dist**2)+(y_dist**2))
                totalforce = (K*p1.q * p2.q)/(dist**2)
                angle = math.atan2(y_dist,x_dist)
                fx = totalforce*math.cos(angle)
                fy = totalforce*math.sin(angle)
                p1.fx += fx
                p1.fy += fy
                if p1 == 2:
                    print(f'---')
                    print(f'debugging: force of particle {j}')
                    print(f'')

    for p in charges:
        p.magf = math.sqrt(p.fx**2 + p.fy**2)
        p.netangle = math.atan2(p.fy,p.fx)
        print(f'For the: {p.q:.2E} C charge @ {p.x},{p.y}:')
        print(f' |Fnet| = {(p.magf):.2E} N')
        print(f'  Fnet  = {p.fx:.2E}i + {p.fy:.2E}j')
        print(f'  Angle = {p.netangle:.2F} rads ({p.netangle*180/math.pi:.2F} deg)\n')
if __name__ == "__main__":
    main()
