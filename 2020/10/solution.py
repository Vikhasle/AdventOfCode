from functools import cache


def read_inp():
    fil = open("bigboy", "r").read().split('\n')
    return [int(x) for x in fil]


def part_one(inp):
    inp.sort()
    vol = 0
    diffs = [0, 0, 1]
    for x in inp:
        diffs[x-vol-1] += 1
        vol = x
    return diffs[0]*diffs[2]


# Easy DFS search with lookup
known_paths = {}


def rec_search(val, inp):
    paths = 0
    if val in known_paths:
        return known_paths[val]
    for v in [1, 2, 3]:
        if val - v == 0:
            paths += 1
        if val-v in inp:
            paths += rec_search(val-v, inp)
    known_paths[val] = paths
    return paths


def part_two(inp):
    return rec_search(max(inp), inp)

# Tribonacci solution


@cache
def trib(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return trib(n-1)+trib(n-2)+trib(n-3)


def solve(inp):
    p, c, prev = 1, 0, 0
    inp.sort()
    for n in inp+[0]:
        if n-prev == 1:
            c += 1
        else:
            p *= trib(c+2)
            c = 0
        prev = n
    return p


print(part_one(read_inp()))
# print(part_two(read_inp()))
print(solve(read_inp()))
