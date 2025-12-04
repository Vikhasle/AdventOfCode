import numpy as np
import re
import sys
import math


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return [pairs.split('-') for pairs in lines[0].split(',')]


def part_one(input):
    total = 0
    for (lo, hi) in input:
        lo, hi = int(lo), int(hi)
        while lo <= hi:
            num_digits = int(math.log(lo, 10)) + 1
            if num_digits % 2 != 0:
                lo = 10**num_digits + 1
                continue
            lhs = lo // (10**(num_digits / 2))
            rhs = lo % (10**(num_digits / 2))
            if lhs == rhs:
                total += lo
            lo += 1
    return total


def part_two(input):
    def invalid(i, num_digits):
        str_i = str(i)
        for j in range(2, num_digits + 1):
            if num_digits % j == 0:
                divided = [str_i[k:k + num_digits//j] for k in range(0, num_digits, num_digits//j)]
                if all(map(lambda x: x == divided[0], divided[1:])):
                    return True

    total = 0
    for (lo, hi) in input:
        lo, hi = int(lo), int(hi)
        while lo <= hi:
            num_digits = int(math.log(lo, 10)) + 1
            if invalid(lo, num_digits):
                total += lo
            lo += 1
    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day2.txt")
    else:
        input = get_input("tests/test2.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
