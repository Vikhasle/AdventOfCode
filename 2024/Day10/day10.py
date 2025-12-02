import numpy as np

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [list(map(lambda x: int(x), line.strip())) for line in file.readlines()]
    return np.array(lines)


def score(map, i, j):
    val = map[i, j]
    total = []
    if i > 0 and map[i - 1, j] - val == 1:
        if map[i - 1, j] == 9:
            total += [(i-1, j)]
        else:
            routes = score(map, i-1, j)
            total += [r for r in routes if r not in total]
    if i < len(map) - 1 and map[i + 1, j] - val == 1:
        if map[i + 1, j] == 9:
            total += [(i+1, j)]
        else:
            routes = score(map, i+1, j)
            total += [r for r in routes if r not in total]
    if j > 0 and map[i, j - 1] - val == 1:
        if map[i, j - 1] == 9:
            total += [(i, j-1)]
        else:
            routes = score(map, i, j-1)
            total += [r for r in routes if r not in total]
    if j < len(map[0]) - 1 and map[i, j + 1] - val == 1:
        if map[i, j + 1] == 9:
            total += [(i, j+1)]
        else:
            routes = score(map, i, j+1)
            total += [r for r in routes if r not in total]
    return total


def score2(map, i, j):
    val = map[i, j]
    total = 0
    if i > 0 and map[i - 1, j] - val == 1:
        if map[i - 1, j] == 9:
            total += 1
        else:
            total += score2(map, i-1, j)
    if i < len(map) - 1 and map[i + 1, j] - val == 1:
        if map[i + 1, j] == 9:
            total += 1
        else:
            total += score2(map, i+1, j)
    if j > 0 and map[i, j - 1] - val == 1:
        if map[i, j - 1] == 9:
            total += 1
        else:
            total += score2(map, i, j-1)
    if j < len(map[0]) - 1 and map[i, j + 1] - val == 1:
        if map[i, j + 1] == 9:
            total += 1
        else:
            total += score2(map, i, j+1)
    return total

def part_one(input):
    N, M = input.shape
    total = 0
    for i in range(N):
        for j in range(M):
            if input[i,j] == 0:
                total += len(score(input, i, j))
    return total


def part_two(input):
    N, M = input.shape
    total = 0
    for i in range(N):
        for j in range(M):
            if input[i,j] == 0:
                total += score2(input, i, j)
    return total


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
