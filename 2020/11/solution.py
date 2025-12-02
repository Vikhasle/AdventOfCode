
def read_inp():
    fil = open("/home/kre213/Koding/AdventOfCode/2020/11/input",
               "r").read().split('\n')
    return [[x for x in y] for y in fil]


def fine_print(inp):
    for line in inp:
        for seat in line:
            print(seat, end="")
        print()


def find_neighbors(inp, i, j):
    n = 0
    for dir_y in [-1, 0, 1]:
        for dir_x in [-1, 0, 1]:
            if dir_y or dir_x:
                if 0 <= i+dir_y < len(inp) and 0 <= j+dir_x < len(inp[i]):
                    if inp[i+dir_y][j+dir_x] == '#':
                        n += 1
    return n


def run_sim(inp):
    change = 0
    to_change = {}
    for i, line in enumerate(inp):
        for j, seat in enumerate(line):
            if seat == 'L' and find_neighbors(inp, i, j) == 0:
                to_change[(i, j)] = '#'
                change += 1
            if seat == '#' and find_neighbors(inp, i, j) >= 4:
                to_change[(i, j)] = 'L'
                change += 1
    for pos in to_change:
        inp[pos[0]][pos[1]] = to_change[pos]
    return change


def sightline(inp, i, j):
    count = 0
    for dir_y in [-1, 0, 1]:
        for dir_x in [-1, 0, 1]:
            if not (dir_x or dir_y):
                continue
            y, x = i+dir_y, j+dir_x
            while 0 <= y < len(inp) and 0 <= x < len(inp[y]):
                if inp[y][x] == "L":
                    break
                if inp[y][x] == "#":
                    count += 1
                    break
                y += dir_y
                x += dir_x
    return count


def run_sim2(inp):
    to_change = {}
    for i, line in enumerate(inp):
        for j, seat in enumerate(line):
            if seat == 'L' and sightline(inp, i, j) == 0:
                to_change[(i, j)] = '#'
            if seat == '#' and sightline(inp, i, j) >= 5:
                to_change[(i, j)] = 'L'

    for pos in to_change:
        inp[pos[0]][pos[1]] = to_change[pos]
    return len(to_change)


def part_one(inp):
    while run_sim(inp) != 0:
        pass
    total = 0
    for line in inp:
        total += line.count('#')
    return total


def part_two(inp):
    while run_sim2(inp) != 0:
        pass
    total = 0
    for line in inp:
        total += line.count('#')
    return total


print(part_one(read_inp()))
print(part_two(read_inp()))
