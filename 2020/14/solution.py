def read_inp():
    fil = open("qh9d5y", "r").read().split("\n")
    return [inst.split(" = ") for inst in fil]


def apply_mask(val, mask):
    bit_string = bin(val)[2:]
    bit_string = "0"*(36-len(bit_string))+bit_string
    new = ""
    for i, bit in enumerate(mask):
        if bit == 'X':
            new += bit_string[i]
        else:
            new += bit
    return int(new, 2)

# inefficient solution


def part_one(inp):
    mask = ""
    mem = {}
    for inst in inp:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            val = apply_mask(int(inst[1]), mask)
            addr = int(inst[0][4:len(inst[0])-1])
            mem[addr] = val
    return sum(mem.values())

# Slightly better


def part1(inp):
    mask = ""
    total = 0
    for inst in inp:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            total += apply_mask(int(inst[1]), mask)
    return total
# FUck part2 is ugly
# Original Retard solution:


def expand_addr(addr):
    new = ""
    for i, bit in enumerate(addr):
        if bit == 'X':
            copy = new
            new += '0'+addr[i+1:]
            copy += '1'+addr[i+1:]
            return (new, copy)
        else:
            new += bit
    return False


def change_addr(addr, mask):
    bit_string = bin(addr)[2:]
    bit_string = "0"*(36-len(bit_string)) + bit_string
    new = ""
    for i, bit in enumerate(mask):
        if bit == '0':
            new += bit_string[i]
        else:
            new += bit
    addrs = [new]
    i = 0
    n = len(addrs)
    while i < n:
        add = addrs[i]
        C = expand_addr(add)
        if C != False:
            addrs.append(C[1])
            addrs[i] = C[0]
            n += 1
        else:
            i += 1
    return addrs


def part_two(inp):
    mask = ""
    mem = {}
    for inst in inp:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            val = int(inst[1])
            addrs = change_addr(int(inst[0][4:len(inst[0])-1]), mask)
            for addr in addrs:
                mem[addr] = val
    return sum(mem.values())


# New smart solution

def part2(inp):
    mask = 0
    total = 0
    for inst in inp:
        if inst[0] == "mask":
            mask = inst[1].count('X')
        else:
            val = int(inst[1])
            total += val*2**mask
    return total


print(part1(read_inp()))
print(part_two(read_inp()))
