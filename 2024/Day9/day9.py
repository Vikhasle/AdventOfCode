from collections import deque

def get_input(file_name):
    with open(file_name, "r") as file:
        return file.read().strip()


def checksum(line):
    total = 0
    for i, c in enumerate(line):
        if c == None:
            continue
        total += i * int(c)
    return total

def part_one(input):
    dot = False
    curr = 0
    mem = []
    chars = 0
    for c in input:
        if dot:
            mem += [None] * int(c)
        else:
            mem += [curr] * int(c)
            curr += 1
        dot = not dot
    defrag = []
    i, j = 0, len(mem) - 1
    while i <= j:
        if mem[i] == None:
            while mem[j] == None and i < j:
                j -= 1
            if mem[j] == None:
                return checksum(defrag)
            defrag.append(mem[j])
            j -= 1
            i += 1
        else:
            defrag.append(mem[i])
            i += 1
    return checksum(defrag)


def part_two(input):
    dot = False
    curr = 0
    mem = []
    empty_sizes = {}
    file_sizes = {}
    file_indexes = {}
    for c in input:
        if dot:
            empty_sizes[len(mem)] = int(c)
            mem += [None] * int(c)
        else:
            file_indexes[curr] = len(mem)
            file_sizes[curr] = int(c)
            mem += [curr] * int(c)
            curr += 1
        dot = not dot
    f_id = curr - 1
    while f_id > 0:
        f_n = file_sizes[f_id]
        f_i = file_indexes[f_id]
        slots = [x for x in empty_sizes.keys() if empty_sizes[x] >= f_n and x < f_i]
        if len(slots) == 0:
            f_id -= 1
            continue
        i = min(slots)
        mem[i : i + f_n]= mem[f_i : f_i + f_n]
        mem[f_i : f_i + f_n] = [None] * f_n
        if f_n < empty_sizes[i]:
            empty_sizes[i+f_n] = empty_sizes[i] - f_n
        empty_sizes[i] = 0
        f_id -= 1
    return checksum(mem)


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
