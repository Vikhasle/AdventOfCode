import numpy as np
import re
import sys

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    total = 0
    for bank in input:
        ratings = [int(x) for x in bank]
        l = max(ratings[:-1])
        r = max(ratings[ratings.index(l) + 1:])
        total += l * 10 + r
    return total


def part_two(input):
    total = 0
    for bank in input:
        start = 0
        ratings = [int(x) for x in bank]
        joltage = 0
        for j in range(12):
            joltage *= 10
            if j == 11:
                bat = np.argmax(ratings[start:]) + start
            else:
                bat = np.argmax(ratings[start:j-11]) + start
            joltage += ratings[bat]
            start = bat + 1
        total += joltage

    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day3.txt")
    else:
        input = get_input("tests/test3.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
