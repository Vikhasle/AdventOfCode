

def read_inp():
    inp = open("input", "r")
    form = [line.strip().split(' ') for line in inp.readlines()]
    return form


def part_one(inp):
    valid = 0
    for line in inp:
        l_bound = int(line[0].split("-")[0])
        h_bound = int(line[0].split("-")[1])
        char = line[1][0]
        if l_bound <= line[2].count(char) <= h_bound:
            valid += 1
    return valid


def part_two(inp):
    valid = 0
    for line in inp:
        i = int(line[0].split("-")[0])
        j = int(line[0].split("-")[1])
        char = line[1][0]
        if (line[2][i-1] == char) ^ (line[2][j-1] == char):
            valid += 1
    return valid


print(part_one(read_inp()))
print(part_two(read_inp()))
