#!/usr/bin/env python3

K = 8.988E9 #Coulombs constant
e = -1.602217662E-19 # charge on electron
class pointCharge():

    """Docstring for pointCharge. """

    def __init__(self, x,y,q):
        self.x = x
        self.y = y
        self.q = q
        self.fx = 0
        self.fy = 0
        self.magf = 0



def main():
    bob = [pointCharge(0,2E-7,2*e), pointCharge(0,0,-3*e), pointCharge(4E-7,0,-5*e)]
    for i, point in enumerate(bob):
        for j, p in enumerate(bob):
            if i != j:
                x_dist = abs(p.x - point.x)
                y_dist = abs(p.y - point.y)
                dist = ((x_dist**2)+(y_dist**2))**.5
                if i == 2:
                    print(f'the distance between them is {dist}.')
                bob[i].magf += (K*point.q * p.q)/(dist**2)
                if i ==2:
                    print(f'the f on the {i}th particle is now {bob[i].magf}')
    for p in bob:
        print(f'The {p.q} C charge @ {p.x},{p.y}')
        print(f'experiences a force of total magnitude {abs(p.magf)} N\n')






if __name__ == "__main__":
    main()
