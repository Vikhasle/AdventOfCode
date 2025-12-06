import numpy as np
import re
import sys
from functools import reduce


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip('\n') for x in file.readlines()]
        return lines


def part_one(input):
    input = [x.split() for x in input]
    exps = [[int(x)] for x in input[0]]
    totals = [0] * len(exps)
    for parts in input[1:-1]:
        for i in range(len(exps)):
            exps[i].append(int(parts[i]))
    for i, op in enumerate(input[-1]):
        if op == '+':
            totals[i] = sum(exps[i])
        else:
            totals[i] = reduce(lambda x, y: x*y, exps[i], 1)

    return sum(totals)


def part_two(input):
    min_len = min([len(x) for x in input])
    ops = input[-1].split()

    dividers = []
    for i in range(min_len):
        if all(map(lambda x: x == ' ', [line[i] for line in input])):
            dividers.append(i)

    new = []
    for line in input[:-1]:
        new_line = []
        for i, div_ind in enumerate(dividers):
            if i != 0:
                new_line.append(line[dividers[i - 1] + 1:div_ind])
            else:
                new_line.append(line[:div_ind])
        new_line.append(line[dividers[-1] + 1:])
        new.append(new_line)

    width = max([len(line[-1]) for line in new])
    for i, line in enumerate(new):
        last = line[-1]
        if len(last) < width:
            new[i][-1] = last + ' ' * (width - len(last))
    total = 0
    for i in range(len(ops)):
        fields = [line[i] for line in new]
        width = max([len(line[i]) for line in new])
        nums = [int("".join([f[j] for f in fields])) for j in range(width)]

        if ops[i] == '+':
            total += sum(nums)
        else:
            total += reduce(lambda x, y: x*y, nums, 1)

    return total



if __name__ == "__main__":
    if len(sys.argv) == 1:
        input =get_input("inputs/day6")
    else:
        input = get_input("tests/test6")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
