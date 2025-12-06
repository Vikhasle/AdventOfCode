import numpy as np
import re
import sys
def get_input(file_name):
    with open(file_name, "r") as file:
        ranges, ings = file.read().split('\n\n')
        ings = ings.strip()
        return [(int(x.split('-')[0]), int(x.split('-')[1])) for x in ranges.split('\n')], [int(x) for x in ings.split('\n')]


def part_one(ranges, ings):
    total = 0
    for num in ings:
        for (min, max) in ranges:
            if min <= num <= max:
                total += 1
                break
    return total


def part_two(ranges, ings):
    total = 0
    counted = []
    ranges.sort(key=lambda x: x[0])  

    for i, (min_r, max_r) in enumerate(ranges):
        concat = False
        for j, (min_c, max_c) in enumerate(counted):
            if (min_r <= max_c or min_c >= max_r):
                counted[j] = (min(min_c, min_r), max(max_c, max_r))
                concat = True
                break
        if not concat:
            counted.append((min_r, max_r))
    
    for (min_c, max_c) in counted:
        total += max_c - min_c + 1
    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day5")
    else:
        input = get_input("tests/test5")
    print("PartOne", part_one(*input))
    print("PartTwo", part_two(*input))
