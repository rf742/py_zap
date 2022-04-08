import csv
import point

def csvout(filename, points):
    with open(filename,'w') as fobj:
        cw = csv.writer(fobj, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cw.writerow(['x','y','q','F_net','F_x','F_y','Angle'])
        for p in points:
            cw.writerow([p.x,p.y,p.q,p.magf,p.fx,p.y,p.netangle])


def getCharges(filename):
    temp = []
    with open(filename, 'r') as fobj:
        for line in fobj:
            if line[0] != "#":
                temp.append(line.strip().split(','))
    points = []
    for element in temp:
            points.append(point.pointCharge(float(element[0]),float(element[1]),float(element[2])))
    return points
