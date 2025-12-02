import numpy as np
import re
import sys
import math


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines[0].split(',')


def part_one(input):
    total = 0
    for id_range in input:
        i = int(id_range.split('-')[0])
        hi = int(id_range.split('-')[1])
        while i <= hi:
            num_digits = int(math.log(i, 10)) + 1
            if num_digits % 2 != 0:
                i = 10**num_digits + 1
                continue
            lhs = i // (10**(num_digits / 2))
            rhs = i % (10**(num_digits / 2))
            if lhs == rhs:
                total += i
            i += 1
    return total


def part_two(input):
    def invalid(i, num_digits):
        for j in range(2, num_digits + 1):
            if num_digits % j == 0:
                divided = [str(i)[k:k + num_digits//j] for k in range(0, num_digits, num_digits//j)]
                if all(map(lambda x: all(map(lambda y: x == y, divided)), divided)):
                    return True

    total = 0
    for id_range in input:
        i = int(id_range.split('-')[0])
        hi = int(id_range.split('-')[1])
        while i <= hi:
            num_digits = int(math.log(i, 10)) + 1
            if invalid(i, num_digits):
                total += i
            i += 1
    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day2.txt")
    else:
        input = get_input("tests/test2.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
