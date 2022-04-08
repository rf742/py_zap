#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table


def tosci(num):
    return f'{num:.2e}'

def printTable(points):
    console=Console()
    table = Table(show_header=True, header_style="bold magenta",)
    table.add_column("x",justify='center')
    table.add_column("y",justify='center')
    table.add_column("q",justify='center')
    table.add_column("Net Force",justify='center')
    table.add_column("F_x",justify='center')
    table.add_column("F_y",justify='center')
    table.add_column("Angle",justify='center')
    for p in points:
        table.add_row(f'{p.x:.2}',f'{p.y:.2}',tosci(p.q),tosci(p.magf),tosci(p.fx),tosci(p.fy),f'{p.netangle:.2}')
    console.print(table)

def uglyprint(points):
    for p in points:
        print(f'For the: {p.q:.2E} C charge @ {p.x},{p.y}:')
        print(f' |Fnet| = {(p.magf):.2E} N')
        print(f'  Fnet  = {p.fx:.2E}i + {p.fy:.2E}j')
        print(f'  Angle = {p.netangle:.2F} rads ({p.netangle*180/math.pi:.2F} deg)\n')
