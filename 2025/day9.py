import numpy as np
import sys
from itertools import combinations

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        lines = [tuple(map(lambda x: int(x), line.split(','))) for line in lines]
        return lines


def area_f(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


def part_one(input):
    return max(map(lambda x: area_f(*x), combinations(input, 2)))


def subset(p0, p1, p2, p3):
    p0_xmax, p0_ymax = max(p0[0], p1[0]), max(p0[1], p1[1])
    p2_xmax, p2_ymax = max(p2[0], p3[0]), max(p2[1], p3[1])
    p0_xmin, p0_ymin = min(p0[0], p1[0]), min(p0[1], p1[1])
    p2_xmin, p2_ymin = min(p2[0], p3[0]), min(p2[1], p3[1])
    return not (p0_xmax <= p2_xmin or
                p0_ymax <= p2_ymin or
                p2_ymax <= p0_ymin or
                p2_xmax <= p0_xmin)


def check_bound(p0, p1, bounds):
    return not any([subset(p0, p1, p2, p3) for (p2, p3) in bounds])


def part_two(input):
    n = len(input)
    min_y, max_y = min(input, key=lambda x:x[1])[1], max(input, key=lambda x:x[1])[1]
    min_x, max_x = min(input, key=lambda x:x[0])[0], max(input, key=lambda x:x[0])[0]

    bounds = []
    for i in range(n):
        curr = input[i]
        next = input[(i + 1) % n]
        bounds.append((curr, next))

    areas = {}

    for i, tile1 in enumerate(input[:-1]):
        for j, tile2 in enumerate(input[i + 1:]):
            areas[area_f(tile1, tile2)] = (tile1, tile2)
    areas_sort = sorted(areas, reverse=True)
    for area in areas_sort:
        tile1, tile2 = areas[area]
        if check_bound(tile1, tile2, bounds):
            return area


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day9")
    else:
        input = get_input("tests/test9")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
