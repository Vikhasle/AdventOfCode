import numpy as np
import re
import sys

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    return


def part_two(input):
    return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/input.txt")
    else:
        input = get_input("tests/test.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
