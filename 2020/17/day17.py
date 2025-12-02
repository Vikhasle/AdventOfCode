import numpy as np
from collections import defaultdict


def find_n(pos, state):
    c = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dz == 0 and dy == 0:
                    continue
                if state[(pos[0] + dz, pos[1] + dy, pos[2] + dx)] == 1:
                    c += 1
    return c


def find_n2(pos, state):
    c = 0
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dw == 0 and dx == 0 and dz == 0 and dy == 0:
                        continue
                    if state[(pos[0] + dw, pos[1] + dz, pos[2] + dy, pos[3] + dx)] == 1:
                        c += 1
    return c


def part_one(state, n, z, N):
    if n == 0:
        return sum(state.values())

    new_state = state.copy()

    for z_level in range(-z, z + 1):
        for i in range(-z, N + z + 1):
            for j in range(-z, N + z + 1):
                n_cubes = find_n((z_level, i, j), state)
                if new_state[(z_level, i, j)]:
                    if not (n_cubes == 2 or n_cubes == 3):
                        new_state[(z_level, i, j)] = 0
                else:
                    if n_cubes == 3:
                        new_state[(z_level, i, j)] = 1

    return part_one(new_state, n - 1, z + 1, N)


def part_two(state, n, z, N):
    if n == 0:
        return sum(state.values())

    new_state = state.copy()

    for w_level in range(-z, z + 1):
        for z_level in range(-z, z + 1):
            for i in range(-z, N + z + 1):
                for j in range(-z, N + z + 1):
                    n_cubes = find_n2((w_level, z_level, i, j), state)
                    if new_state[(w_level, z_level, i, j)]:
                        if not (n_cubes == 2 or n_cubes == 3):
                            new_state[(w_level, z_level, i, j)] = 0
                    else:
                        if n_cubes == 3:
                            new_state[(w_level, z_level, i, j)] = 1

    return part_two(new_state, n - 1, z + 1, N)


def main():
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")
        lines.remove(lines[-1])
        state = [[1 if x == "#" else 0 for x in line] for line in lines]
    n = len(state)
    start_state = defaultdict(lambda: 0)
    for y in range(n):
        for x in range(n):
            start_state[(0, 0, y, x)] = state[y][x]
    final = part_two(start_state, 6, 1, n)
    print(final)


if __name__ == "__main__":
    main()
