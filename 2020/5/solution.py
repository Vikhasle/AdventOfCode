import sys


def read_inp():
    fil = open(sys.argv[1], "r").read().translate(
        str.maketrans("FBRL", "0110"))
    return [int(x, 2) for x in fil.split("\n")]


def part_one(inp):
    return max(inp)


def part_two(inp):
    return sum(range(min(inp), max(inp)+1))-sum(inp)


print(part_one(read_inp()))
print(part_two(read_inp()))
