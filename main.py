#!/usr/bin/env python3
import sys
import math
import argparse
import csv
import time
import tables
K = 8.988E9 # Coulomb constant
e = -1.602217662E-19 # charge on electron
G = 6.674E-11 # Gravitational constant

def csvout(filename, points):
    with open(filename,'w') as fobj:
        cw = csv.writer(fobj, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cw.writerow(['x','y','q','F_net','F_x','F_y','Angle'])
        for p in points:
            cw.writerow([p.x,p.y,p.q,p.magf,p.fx,p.y,p.netangle])
        
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gravity', action='store_true', help='The program will compute gravitational force instead of electrical force. [Put mass where charge normally goes in input file]')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-i', '--input-data', action='store', dest='infile', required='true', help='File containingdata on your point charges [x,y,q] ')
    parser.add_argument('-c', '--csv', action='store_true', help='output data to csv')
    return parser.parse_args()

class pointCharge():
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
        self.fx = 0
        self.fy = 0
        self.magf = 0
        self.netangle = 0

def getCharges(filename):
    temp = []
    with open(filename, 'r') as fobj:
        for line in fobj:
            if line[0] != "#":
                temp.append(line.strip().split(','))
    points = []
    for element in temp:
            points.append(pointCharge(float(element[0]),float(element[1]),float(element[2])))
    return points

def validate_masses(points):
    for p in points:
        if p.q < 0:
            print("In gravity mode the masses must always be positive")
            print("Exiting")
            sys.exit(1)

def main():
    args = get_args()
    verbose = args.verbose
    csvoutput=args.csv
    FORMULACONSTANT = K if not args.gravity else G
    charges = getCharges(args.infile)
    if args.gravity:
        validate_masses(charges)
    for i, p1 in enumerate(charges):
        for j, p2 in enumerate(charges):
            if i != j:
                x_dist = abs(p2.x - p1.x)
                y_dist = abs(p2.y - p1.y)
                dist = math.sqrt((x_dist**2)+(y_dist**2))
                totalforce = (FORMULACONSTANT*p1.q * p2.q)/(dist**2)
                angle = math.atan2(y_dist,x_dist)
                fx = abs(totalforce*math.cos(angle))
                fy = abs(totalforce*math.sin(angle))
                if not args.gravity:
                    if p2.x < p1.x and (p1.q * p2.q < 0):
                        fx=-fx
                    elif p2.x > p1.x and (p1.q * p2.q > 0):
                        fx=-fx
                    if p2.y < p1.y and (p1.q * p2.q < 0):
                        fy=-fy
                    elif p2.y > p1.y and (p1.q * p2.q > 0):
                        fy=-fy
                elif args.gravity:
                    if p2.x < p1.x:
                        fx=-fx
                    if p2.y < p1.y:
                        fy=-fy
                else:
                    print("Error, exiting")
                    sys.exit(1)
                p1.fx += fx
                p1.fy += fy
                if verbose:
                    print(f'--- Verbose Output ---')
                    print(f'force of particle {j} on particle {i}')
                    print(f'fx = {fx:.2E}')
                    print(f'fy = {fy:.2E}')
                    print(f'y: {p2.y}-{p1.y} = {p2.y-p1.y}')
                    print(f'x: {p2.x}-{p1.x} = {p2.x-p1.x}')
                    print(f'Fnet = {math.hypot(fx,fy):.2E}')
                    print(f'angle = {angle*180/math.pi:.2F}')
                    print(f'----------------------\n')
    for p in charges:
        p.magf = math.sqrt(p.fx**2 + p.fy**2)
        p.netangle = math.atan2(p.fy,p.fx)
    if csvoutput:
        csvfilename = 'zap_data_' + time.strftime('%Y%m%d%H%M%S') + '.csv'
        csvout(csvfilename, charges)
        if verbose:
            print("writing csv data to: " + csvfilename)
    try:
        tables.printTable(charges)
    except:
        if verbose:
            print("Tables not working, defaulting to ugly printing")
        tables.uglyprint(charges)
if __name__ == "__main__":
    main()
