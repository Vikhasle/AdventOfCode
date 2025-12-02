import numpy as np


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip().split(', ') for x in file.readlines()]
        lines = [(int(x[0]), int(x[1])) for x in lines]
        return lines


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part_one(input):
    max_y = max(input, key=lambda x: x[1])[1] + 1
    max_x = max(input, key=lambda x: x[0])[0] + 2

    disq = set()
    dist_map = []

    for i in range(0, max_y):
        for j in range(0, max_x):
            dists = [dist(p, (j, i)) for p in input]
            if dists.count(min(dists)) > 1:
                dist_map.append('.')
                continue
            if i == 0 or i == max_x - 1 or j == 0 or j == max_y - 1:
                disq.add(np.argmin(dists))
            dist_map.append(np.argmin(dists))
    counts = []
    for i in range(len(input)):
        if i not in disq:
            counts.append(dist_map.count(i))

    return max(counts)


def part_two(input):
    max_y = max(input, key=lambda x: x[1])[1] + 1
    max_x = max(input, key=lambda x: x[0])[0] + 2

    safe_spots = 0

    for i in range(0, max_y):
        for j in range(0, max_x):
            dists = [dist(p, (j, i)) for p in input]
            if np.sum(dists) < 10000:
                safe_spots += 1

    return safe_spots


if __name__ == "__main__":
    input = get_input("input6.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
