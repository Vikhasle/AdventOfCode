import sys


def read_inp():
    inp = open(sys.argv[1], "r")
    form = [int(line) for line in inp.readlines()]
    return form


def part_one(inp):
    for i, n in enumerate(inp):
        if 99920044-n in inp[i:]:
            return n*(99920044-n)


def part_two(inp):
    for i, n in enumerate(inp):
        for j, m in enumerate(inp[i:]):
            if 2020-n-m in inp[j:]:
                return n*m*(2020-n-m)


def dict_sol(inp):
    inp.sort()
    dic = {}
    for i, n in enumerate(inp):
        for _, m in enumerate(inp[i:]):
            dic[n+m] = n*m

    for n in inp:
        if dic.get(99920044-n) != None:
            return dic[99920044-n]*n


def wiki_sol(inp):
    inp.sort()
    for i in range(len(inp)-2):
        a = inp[i]
        start = i+1
        end = len(inp)-1
        while(start < end):
            b = inp[start]
            c = inp[end]
            if a+b+c == 2020:
                return a*b*c
            elif a+b+c > 2020:
                end -= 1
            else:
                start += 1


print(wiki_sol(read_inp()))
