#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
import math


tosci = lambda num: f'{num:.2e}'


def printTable(points, angleUnit):
    console=Console()
    table = Table(show_header=True, header_style="bold magenta",)
    headers = ["x","y","q","Net Force", "F_x", "F_y", "Angle"]
    for i in headers:
        table.add_column(str(i), justify='center')
    for p in points:
        mag, ang = p.resolve(angleUnit)
        table.add_row(f'{p.x:.2}',f'{p.y:.2}',tosci(p.q),tosci(mag),tosci(p.fx),tosci(p.fy),f'{ang:.2f}')
    console.print(table)

def uglyprint(points):
    for p in points:
        mag, ang = p.resolve()
        print(f'For the: {p.q:.2E} C charge @ {p.x},{p.y}:')
        print(f' |Fnet| = {mag:.2E} N')
        print(f'  Fnet  = {p.fx:.2E}i + {p.fy:.2E}j')
        print(f'  Angle = {ang:.2F} rads ({p.resolve(True)[1]:.2F} deg)')
        print('\n')

def pTable(points, deg):
    try:
        printTable(points,deg)
    except:
        print("Error: Defaulting to plain text output")
        uglyprint(points)

