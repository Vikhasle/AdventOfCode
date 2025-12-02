import numpy as np
from collections import defaultdict

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def part_one(input):
    N, M = len(input), len(input[0])
    antinodes = np.zeros((N, M))
    freqs = defaultdict(list)
    for i in range(N):
        for j in range(M):
            if input[i][j] == '.':
                continue
            freqs[input[i][j]].append((i, j))

    for _, (_, antennas) in enumerate(freqs.items()):
        for i, a1 in enumerate(antennas[:-1]):
            for j, a2 in enumerate(antennas[i+1:]):
                di = a1[0] - a2[0]
                dj = a1[1] - a2[1]
                p1 = (a1[0] + di, a1[1] + dj)
                p2 = (a2[0] - di, a2[1] - dj)
                if 0 <= p1[0] < N and 0 <= p1[1] < M:
                    antinodes[*p1] = max(1, antinodes[*p1])
                if 0 <= p2[0] < N and 0 <= p2[1] < M:
                    antinodes[*p2] = max(1, antinodes[*p2])

    for i in range(N):
        for j in range(M):
            if input[i][j] != '.':
                print(input[i][j], end="")
            elif antinodes[i, j] == 1:
                print('#', end="")
            else:
                print(".", end="")
        print()
    return np.sum(antinodes)


def part_two(input):
    N, M = len(input), len(input[0])
    antinodes = np.zeros((N, M))
    freqs = defaultdict(list)
    for i in range(N):
        for j in range(M):
            if input[i][j] == '.':
                continue
            freqs[input[i][j]].append((i, j))

    for _, (_, antennas) in enumerate(freqs.items()):
        for i, a1 in enumerate(antennas[:-1]):
            for j, a2 in enumerate(antennas[i+1:]):
                di = a1[0] - a2[0]
                dj = a1[1] - a2[1]
                p1 = (a1[0], a1[1])
                p2 = (a2[0], a2[1])
                while 0 <= p1[0] < N and 0 <= p1[1] < M:
                    antinodes[*p1] = max(1, antinodes[*p1])
                    p1 = (p1[0] + di, p1[1] + dj)
                while 0 <= p2[0] < N and 0 <= p2[1] < M:
                    antinodes[*p2] = max(1, antinodes[*p2])
                    p2 = (p2[0] - di, p2[1] - dj)

    for i in range(N):
        for j in range(M):
            if input[i][j] != '.':
                print(input[i][j], end="")
            elif antinodes[i, j] == 1:
                print('#', end="")
            else:
                print(".", end="")
        print()
    return np.sum(antinodes)


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
