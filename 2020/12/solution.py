from math import *


def read_inp():
    fil = open("test2", "r").read().split("\n")
    return fil


def manhattan_dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def move_ship(ship, dir, units):
    ship[0] += dir[0]*units
    ship[1] += dir[1]*units


def part_one(inp):
    dir = [1, 0]
    deg = 0
    ship = [0, 0]
    cardinals = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }
    for inst in inp:
        if inst[0] in cardinals:
            move_ship(ship, cardinals[inst[0]], int(inst[1:]))
        if inst[0] == 'R':
            deg -= radians(int(inst[1:]))
            dir[0] = int(cos(deg))
            dir[1] = int(sin(deg))
        if inst[0] == 'L':
            deg += radians(int(inst[1:]))
            dir[0] = int(cos(deg))
            dir[1] = int(sin(deg))
        if inst[0] == 'F':
            move_ship(ship, dir, int(inst[1:]))
    return manhattan_dist(ship, (0, 0))


def part_two(inp):
    wpoint = [10, 1]
    ship = [0, 0]
    deg = atan(wpoint[1]/wpoint[0])
    cardinals = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }
    for inst in inp:
        if inst[0] in cardinals:
            move_ship(wpoint, cardinals[inst[0]], int(inst[1:]))
            if wpoint[0] > 0:
                deg = atan(wpoint[1]/wpoint[0])
            elif wpoint[0] < 0 and wpoint[1] > 0:
                deg = atan(wpoint[1]/wpoint[0])-pi
            elif wpoint[0] < 0:
                deg = atan(wpoint[1]/wpoint[0])+pi
            else:
                deg = wpoint[1]/abs(wpoint[1])*pi/2
        if inst[0] == 'L':
            deg += radians(int(inst[1:]))
            r = sqrt(wpoint[0]**2+wpoint[1]**2)
            wpoint[0] = cos(deg)*r
            wpoint[1] = sin(deg)*r
        if inst[0] == 'R':
            deg -= radians(int(inst[1:]))
            r = sqrt(wpoint[0]**2+wpoint[1]**2)
            wpoint[0] = cos(deg)*r
            wpoint[1] = sin(deg)*r
        if inst[0] == 'F':
            move_ship(ship, wpoint, int(inst[1:]))
    return round(abs(ship[0])+abs(ship[1]))


print(part_one(read_inp()))
print(part_two(read_inp()))
