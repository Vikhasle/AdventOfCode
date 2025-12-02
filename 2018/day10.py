import numpy as np
import re
import sys
from copy import deepcopy

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    points = []
    vels = []
    for line in input:
        points.append([0,0])
        vels.append([0,0])
        split_pos = line.find(',')
        end_pos = line.find('>')
        points[-1][0] = int(line[10:split_pos])
        points[-1][1] = int(line[split_pos + 1:end_pos])
        line = line[end_pos + 1:]
        split_pos = line.find(',')
        end_pos = line.find('>')
        vels[-1][0] = int(line[11:split_pos])
        vels[-1][1] = int(line[split_pos + 1:end_pos])

    while True:
        max_x, min_x = 0, 0
        max_y, min_y = 0, 0
        for i, p in enumerate(points):
            p[0] += vels[i][0]
            p[1] += vels[i][1]
            max_x = max(p[0], max_x)
            min_x = min(p[0], min_x)
            max_y = max(p[1], max_y)
            min_y = min(p[1], min_y)
        
        lines = []
        used = []
        for i, p1 in enumerate(points):
            if i in used:
                continue
            lines.append([p1])
            for j,p2 in enumerate(points[i:]):
                if p1[0] == p2[0] and abs(p1[1] - p2[1]) < 7:
                    lines[-1].append(p2)
                    used.append(j)
        if sum(map(lambda x: len(x) > 5, lines)) > 10:
            for line in lines:
                if len(line) > 5:

        if abs(max_y - min_y) < 200:
            for i in range(min_y, max_y + 1):
                for j in range(min_x, max_x):
                    if [j, i] in points:
                        print("#", end="")
                    else:
                        print(".", end="")
                print()

            return

def part_two(input):
    return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/input10.txt")
    else:
        input = get_input("tests/test10.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
