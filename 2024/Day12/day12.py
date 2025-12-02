from collections import defaultdict
import numpy as np


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def is_edge(input, i, j):
    val = input[i][j]
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]
    p_count = 0
    for di, dj in zip(dis, djs):
        if (not 0 <= i + di < len(input)) or (not 0 <= j + dj < len(input[0])) or input[i + di][j + dj] != val:
            p_count += 1
    return p_count


def region(input, i, j, visited):
    visited[i, j] = 1
    val = input[i][j]
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]
    area = 1
    per = is_edge(input, i, j)
    for di, dj in zip(dis, djs):
        if 0 <= i + di < len(input) and 0 <= j + dj < len(input[0]) and input[i + di][j + dj] == val:
            if visited[i+di, j+dj]:
                continue
            temp = region(input, i + di, j + dj, visited)
            area += temp[0]
            per += temp[1]
    return area, per


def part_one(input):
    N, M = len(input), len(input[0])
    total = 0
    visited = np.zeros((N,M))
    for i in range(len(input)):
        for j, c in enumerate(input[i]):
            if visited[i,j]:
                continue
            area, perimeter = region(input, i, j, visited)
            total += area * perimeter
    return total


def is_side(input, i, j):
    val = input[i][j]
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]
    p_count = 0
    for di, dj in zip(dis, djs):
        if (not 0 <= i + di < len(input)) or (not 0 <= j + dj < len(input[0])) or input[i + di][j + dj] != val:
            p_count += 1
    return p_count


def region2(input, i, j, visited):
    N, M = len(input), len(input[0])
    visited[i, j] = 1
    val = input[i][j]
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]
    area = 1
    vert_sides = set()
    hor_sides = set()
    for di, dj in zip(dis, djs):
        if not (0 <= di + i < N and 0 <= dj + j < M) or input[i+di][j+dj] != val:
            if di:
                vert_sides.add((i, di))
            else:
                hor_sides.add((j, dj))
        elif visited[i + di, j + dj]:
            continue
        else:
            d_area, d_vert, d_hor = region2(input, i+di, j+dj, visited)
            area += d_area
            vert_sides = vert_sides.union(d_vert)
            hor_sides = hor_sides.union(d_hor)
    return area, vert_sides, hor_sides


def part_two(input):
    N, M = len(input), len(input[0])
    total = 0
    visited = np.zeros((N,M))
    for i in range(len(input)):
        for j, c in enumerate(input[i]):
            if visited[i,j] == 1:
                continue
            area, v_sides, h_sides = region2(input, i, j, visited)
            print(c, area, v_sides, h_sides)
            total += area * (len(v_sides) + len(h_sides))
    return total


if __name__ == "__main__":
    input = get_input("test.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
