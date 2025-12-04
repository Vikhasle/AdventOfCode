import numpy as np
import re
import sys


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def num_neigh(grid, i, j, N, M):
    n = int(i > 0 and grid[i-1][j] == '@')
    n += int(i < N - 1 and grid[i+1][j] == '@')
    n += int(j > 0 and grid[i][j-1] == '@')
    n += int(j < M - 1 and grid[i][j + 1] == '@')
    n += int(i > 0 and j < M - 1 and grid[i - 1][j + 1] == '@')
    n += int(i < N - 1 and j < M - 1 and grid[i + 1][j + 1] == '@')
    n += int(i > 0 and j > 0 and grid[i - 1][j - 1] == '@')
    n += int(i < N - 1 and j > 0 and grid[i + 1][j - 1] == '@')

    return n


def part_one(input):
    N, M = len(input), len(input[0])
    total = 0

    for i in range(N):
        for j in range(M):
            if input[i][j] == '@' and num_neigh(input, i, j, N, M) < 4:
                total += 1

    return total


def part_two(input):
    N, M = len(input), len(input[0])
    total = 0
    old_total = -1
    
    while old_total != total:
        old_total = total
        for i in range(N):
            for j in range(M):
                if input[i][j] == '@' and num_neigh(input, i, j, N, M) < 4:
                    total += 1
                    input[i] = input[i][:j] + '.' + input[i][j+1:]
    return total


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day4")
    else:
        input = get_input("tests/test4")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
