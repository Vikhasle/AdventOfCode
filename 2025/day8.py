import numpy as np
import sys


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        lines = [list(map(lambda x: int(x), line.split(','))) for line in lines]
        return lines


def part_one(input):
    n = len(input)
    dist_map = np.zeros((n, n))
    for i, pos in enumerate(input[:-1]):
        for j, pos2 in enumerate(input[i + 1:]):
            diff = [pos[k] - pos2[k] for k in range(len(pos))]
            dist = np.linalg.norm(diff)
            dist_map[i, j + i + 1] = dist
            dist_map[j + i + 1, i] = dist
    for i in range(n):
        dist_map[i, i] = np.inf
    circuits = []
    circuit_map = {}
    for _ in range(1000):
        i, j = np.argmin(dist_map) // n, np.argmin(dist_map) % n
        dist_map[i, j] = np.inf
        dist_map[j, i] = np.inf
        if i in circuit_map and j in circuit_map:
            c_i, c_j = circuit_map[i], circuit_map[j]
            if c_i != c_j:
                for c_p in circuits[c_j]:
                    circuit_map[c_p] = c_i
                circuits[c_i] += circuits[c_j]
                circuits.pop(c_j)
                for c in circuits[c_j:]:
                    for box in c:
                        circuit_map[box] -= 1
        elif i in circuit_map:
            c_i = circuit_map[i]
            circuit_map[j] = c_i
            circuits[c_i].append(j)
        elif j in circuit_map:
            c_j = circuit_map[j]
            circuit_map[i] = c_j
            circuits[c_j].append(i)
        else:
            circuit_map[i] = len(circuits)
            circuit_map[j] = len(circuits)
            circuits.append([i, j])
    sizes = sorted([len(c) for c in circuits])[::-1]
    return sizes[0]*sizes[1]*sizes[2]


def part_two(input):
    n = len(input)
    dist_map = np.zeros((n, n))
    for i, pos in enumerate(input[:-1]):
        for j, pos2 in enumerate(input[i + 1:]):
            diff = [pos[k] - pos2[k] for k in range(len(pos))]
            dist = np.linalg.norm(diff)
            dist_map[i, j + i + 1] = dist
            dist_map[j + i + 1, i] = dist
    circuits = []
    c_map = []
    for i in range(n):
        dist_map[i, i] = np.inf
        circuits.append([i])
        c_map.append(i)
    i, j = 0, 0
    while len(circuits) > 1:
        i, j = np.argmin(dist_map) // n, np.argmin(dist_map) % n
        c_i, c_j = c_map[i], c_map[j]
        dist_map[i, j] = np.inf
        dist_map[j, i] = np.inf
        if c_i == c_j:
            continue
        for c_p in circuits[c_j]:
            c_map[c_p] = c_i
        circuits[c_i] += circuits[c_j]
        circuits.pop(c_j)
        for c in circuits[c_j:]:
            for box in c:
                c_map[box] -= 1
    return input[i][0] * input[j][0]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        input = get_input("inputs/day8")
    else:
        input = get_input("tests/test8")
    #print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
