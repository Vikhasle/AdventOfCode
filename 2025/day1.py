import numpy as np
import re
import sys


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    dial = 50
    score = 0
    for rot in input:
        dir = -1 if rot[0] == 'L' else 1
        mag = int(rot[1:])
        dial += mag * dir
        dial = dial % 100
        if dial == 0:
            score += 1
    return score


def part_two(input): 
    dial = 50
    score = 0
    for rot in input:
        dir = -1 if rot[0] == 'L' else 1
        mag = int(rot[1:])
        new_dial = (dial + mag * dir)
        score += abs(dial - new_dial) // 100
        new_dial = new_dial % 100
        if new_dial <= dial and dir == 1:
            score += 1
        elif dial != 0 and new_dial >= dial and dir == -1:
            score += 1
        elif new_dial == 0:
            score += 1
        dial = new_dial
    return score


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day1.txt")
    else:
        input = get_input("tests/test1.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
