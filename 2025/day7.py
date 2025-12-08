import numpy as np
import sys
from functools import cache


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    beams = set()
    beams.add(input[0].index('S'))
    splits = 0
    for i in range(1, len(input)):
        new_beams = set()
        for p in beams:
            if input[i][p] == '^':
                splits += 1
                new_beams.add(p - 1)
                new_beams.add(p + 1)
            else:
                new_beams.add(p)
        beams = new_beams
    return splits


def part_two(input):
    @cache
    def traverse(i, j):
        if i == len(input) - 1:
            return 1
        elif input[i][j] == '^':
            return traverse(i, j-1) + traverse(i, j+1)
        else:
            return traverse(i+1, j)

    start = input[0].index('S')
    i = 1
    return traverse(i, start)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day7")
    else:
        input = get_input("tests/test7")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
