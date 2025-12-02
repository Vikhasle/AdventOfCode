import numpy as np

def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


vel = {
        'up' : (-1,0),
        'down' : (1,0),
        'left' : (0,-1),
        'right' : (0,1),
        }

turn = {
        'up' : 'right',
        'right': 'down',
        'down': 'left',
        'left': 'up'
        }


def part_one(input):
    i, j = 0, 0
    while '^' not in input[i]:
        i += 1
    j = input[i].index('^')
    N, M = len(input), len(input[0])
    curr_dir = 'up'
    visited = np.zeros(N*M)
    while 0 <= i < N and 0 <= j < M:
        visited[i * M + j] = max(1, visited[i * M + j])
        di, dj = vel[curr_dir]
        if 0 <= i + di < N and 0 <= j + dj < M and input[i + di][j + dj] == '#':
            curr_dir = turn[curr_dir]
        i += vel[curr_dir][0]
        j += vel[curr_dir][1]
    return sum(visited)


def cycle(input, obs_i, obs_j):
    i, j = 0, 0
    while '^' not in input[i]:
        i += 1
    j = input[i].index('^')
    curr_dir = 'up'
    di, dj = vel[curr_dir]

    N, M = len(input), len(input[0])
    hits = []

    while 0 <= i + di < N and 0 <= j + dj < M:
        while (input[i + di][j + dj] == '#') or (i + di == obs_i and j + dj == obs_j):
            for h in hits:
                if h[0] == curr_dir and h[1] == (i + di) * M + j + dj:
                    return True
            hits.append((curr_dir, (i + di)*M + j + dj))
            curr_dir = turn[curr_dir]
            di, dj = vel[curr_dir]
        i += di
        j += dj
    return False


def part_two(input):
    i, j = 0, 0
    while '^' not in input[i]:
        i += 1
    j = input[i].index('^')
    N, M = len(input), len(input[0])
    curr_dir = 'up'
    total = 0
    di, dj = vel[curr_dir]
    positions = []
    while 0 <= i + di < N and 0 <= j + dj < M:
        if input[i + di][j + dj] == '#':
            curr_dir = turn[curr_dir]
            di, dj = vel[curr_dir]
        if (i + di, j + dj) not in positions:
            positions.append((i + di, j + dj))
        i += di
        j += dj
    for p in positions:
        if cycle(input, p[0], p[1]):
            total += 1
    return total


if __name__ == "__main__":
    input = get_input("input")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
