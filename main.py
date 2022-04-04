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
#    charges = [pointCharge(0,-1,1),pointCharge(0,0,2), pointCharge(math.sqrt(3),0,-3)]
#    charges = [pointCharge(0,0,4E-9),pointCharge(5E-2,0,6E-9),pointCharge(0,3E-2,-3E-9)]
    charges = [pointCharge(0,2E-7,2*e), pointCharge(0,0,-3*e), pointCharge(4E-7,0,-5*e)]
#    charges = [pointCharge(0,4,-6E-6), pointCharge(0,0,4E-6), pointCharge(3,0,2E-6)]
#   see https://farside.ph.utexas.edu/teaching/316/lectures/node20.html

    for i, p1 in enumerate(charges):
        for j, p2 in enumerate(charges):
            if i != j:
                x_dist = abs(p2.x - p1.x)
                y_dist = abs(p2.y - p1.y)
                dist = math.sqrt((x_dist**2)+(y_dist**2))
                totalforce = (K*p1.q * p2.q)/(dist**2)
                angle = math.atan2(y_dist,x_dist)
                fx = abs(totalforce*math.cos(angle))
                fy = abs(totalforce*math.sin(angle))
                if p2.x < p1.x and (p1.q * p2.q < 0):
                    fx=-fx
                elif p2.x > p1.x and (p1.q * p2.q > 0):
                    fx=-fx
                if p2.y < p1.y and (p1.q * p2.q < 0):
                    fy=-fy
                elif p2.y > p1.y and (p1.q * p2.q > 0):
                    fy=-fy
                p1.fx += fx
                p1.fy += fy
                print(f'---')
                print(f'debugging: force of particle {j+1} on particle {i+1}')
                print(f'debugging: fx = {fx:.2E} = cos of atan[{y_dist}, {x_dist}]')
                print(f'debugging: fy = {fy:.2E}')
                print(f'debugging: y: {p2.y}-{p1.y} = {p2.y-p1.y}')
                print(f'debugging: x: {p2.x}-{p1.x} = {p2.x-p1.x}')
                print(f'debugging: Fnet = {math.hypot(fx,fy):.2E}')
                print(f'debugging: angle = {angle*180/math.pi:.2F}')
                print(f'---')

    for p in charges:
        p.magf = math.sqrt(p.fx**2 + p.fy**2)
        p.netangle = math.atan2(p.fy,p.fx)
        print(f'For the: {p.q:.2E} C charge @ {p.x},{p.y}:')
        print(f' |Fnet| = {(p.magf):.2E} N')
        print(f'  Fnet  = {p.fx:.2E}i + {p.fy:.2E}j')
        print(f'  Angle = {p.netangle:.2F} rads ({p.netangle*180/math.pi:.2F} deg)\n')
if __name__ == "__main__":
    main()
