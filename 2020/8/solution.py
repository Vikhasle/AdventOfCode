def read_inp():
    fil = open("input", "r").read().split('\n')
    return [x.split(" ") for x in fil]


def part_one(inp):
    acc = 0
    ip = 0
    visited = set()
    while ip not in visited:
        op = inp[ip]
        visited.add(ip)
        if op[0] == "acc":
            acc += int(op[1][1:])
        if op[0] == "jmp":
            ip += int(op[1])
        else:
            ip += 1
    return acc


def part_two(inp):
    jmps = [x for x in range(len(inp)) if inp[x][0] == "jmp"]
    for jmp in jmps:
        acc = 0
        ip = 0
        visited = set()
        while ip < len(inp):
            if ip in visited:
                break
            visited.add(ip)
            op = inp[ip]
            if op[0] == "nop" or ip == jmp:
                ip += 1
            elif op[0] == "acc":
                acc += int(op[1])
                ip += 1
            elif op[0] == "jmp":
                ip += int(op[1])
        if ip == len(inp):
            return acc


print(part_one(read_inp()))

print(part_two(read_inp()))
