def read_inp():
    #fil = open("input", "r").read()
    fil = open("bigboy", "r").read()
    return [int(x) for x in fil.split()]


def part_one(inp):
    # for i, num in enumerate(inp[25:]):
    for i, num in enumerate(inp[125:]):
        #index = i+25
        index = i+125
        found = False
        # for b in inp[index-25:index]:
        for b in inp[index-125:index]:
            # if num - b in inp[index-25:index]:
            if num - b in inp[index-125:index]:
                found = True
                break
        if not found:
            return num


# O(n) solution part2 from /g/
def part_two(inp, target):
    q = []
    total = 0
    for num in inp:
        total += num
        q.append(num)
        while (total > target):
            total -= q[0]
            q.pop(0)
        if total == target:
            return min(q)+max(q)


# Brute force solution
"""
def part_two(inp, target):
    for i, _ in enumerate(inp):
        for j, _ in enumerate(inp[i+1:]):
            if sum(inp[i:j]) == target:
                return min(inp[i:j])+max(inp[i:j])
"""

p1 = part_one(read_inp())
print(p1)
print(part_two(read_inp(), p1))
