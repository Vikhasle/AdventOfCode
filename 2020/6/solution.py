def read_inp():
    fil = open("/home/kre213/Koding/AdventOfCode/2020/6/input",
               "r").read().split('\n\n')
    return fil


def part_one(inp):
    total = 0
    for group in inp:
        c = [set(q) for q in group.split()]
        total += len(set.union(*c))
    return total


def part_two(inp):
    total = 0
    for group in inp:
        c = [set(q) for q in group.split()]
        total += len(set.intersection(*c))
    return total


print(part_one(read_inp()))
print(part_two(read_inp()))
