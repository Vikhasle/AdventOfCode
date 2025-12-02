def read_inp():
    inp = open("input", "r").read().split("\n")
    return inp


def part_one(inp):
    pos = [0, 0]
    trees = 0
    while pos[0] != len(inp)-1:
        if inp[pos[0]][pos[1]] == "#":
            trees += 1
        pos[1] = (pos[1]+3) % len(inp[pos[0]])
        pos[0] += 1
    return trees


def part_two(inp):
    vels = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    total = 1
    for vel in vels:
        pos = [0, 0]
        trees = 0
        while pos[1] < len(inp)-1:
            if inp[pos[1]][pos[0]] == "#":
                trees += 1
            pos[0] = (pos[0]+vel[0]) % len(inp[pos[1]])
            pos[1] += vel[1]
        print(trees)
        total *= trees
    return total


print(part_one(read_inp()))
print(part_two(read_inp()))
