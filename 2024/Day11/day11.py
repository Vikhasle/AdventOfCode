from math import log10

from functools import cache

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()][0]
        lines = [int(x) for x in lines.split(' ')]
        return lines


@cache
def steps(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return steps(1, n - 1)
    n_dig = int(log10(stone)) + 1
    if n_dig % 2 == 0:
        return steps(stone // 10**(n_dig/2), n-1) + steps(stone % 10**(n_dig/2), n-1)
    else:
        return steps(stone * 2024, n - 1)


def part_one(input):
    return sum([steps(s, 25) for s in input])


def part_two(input):
    return sum([steps(s, 75) for s in input])


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
