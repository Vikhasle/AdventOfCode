def read_inp():
    return [8, 11, 0, 19, 1, 2]


def part_one(inp):
    seen = inp
    for i in range(len(inp), 2020):
        last = seen[i-1]
        if seen.count(last) > 1:
            j = i-2
            while seen[j] != last:
                j -= 1
            seen.append(i-j-1)
        else:
            seen.append(0)
    return seen[2019]


def part_two(inp):
    seen = inp
    larger = {}
    for i in range(1, len(inp)):
        larger[inp[i-1]] = i-1
    for i in range(len(inp), 30000000):
        last = seen[i-1]
        if last in larger:
            seen.append(i-larger[last]-1)
            larger[last] = i-1
        else:
            larger[last] = i-1
            seen.append(0)
    return seen[30000000-1]


print(part_one(read_inp()))
print(part_two(read_inp()))
