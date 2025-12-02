import re
num_expr = re.compile("[0-9]+")
ast_expr = re.compile(r"\*")


def get_input(file_name):
    with open(file_name, "r") as file:
        lines = [x.strip() for x in file.readlines()]
        return lines


def find_symbol(line, start, end):
    for k in range(start, end + 1):
        if line[k] != "." and not line[k].isdigit():
            return True
    return False


def is_adj(input, i, j, len_match):
    start = max(i - 1, 0)
    end = min(i + len_match, len(input[j]) - 1)
    if j != 0 and find_symbol(input[j-1], start, end):
        return True
    if j != len(input) -1 and find_symbol(input[j+1], start, end):
        return True
    if input[j][start] != "." and not input[j][start].isdigit():
        return True
    if input[j][end] != "." and not input[j][end].isdigit():
        return True
    return False


def part_one(input):
    sum = 0
    for j, line in enumerate(input):
        i = 0
        while match := num_expr.search(line[i:]):
            if is_adj(input, i + match.start(), j, len(match.group())):
                sum += int(match.group())
            i += match.end()
    return sum


def search_line(line, start, end):
    ns = []
    k = 0
    while (num_match := num_expr.search(line[k:])) and k <= end:
        if num_match.end() + k > start and num_match.start() + k <= end:
            ns.append(int(num_match.group()))
        k += num_match.end()
    return ns


def find_n(input, i, j):
    ns = []
    start = max(i - 1, 0)
    end = min(i + 1, len(input[j]) - 1)
    if j != 0:
        ns += search_line(input[j-1], start, end)
    if j != len(input) - 1:
        ns += search_line(input[j+1], start, end)
    ns += search_line(input[j], start, end)
    if len(ns) != 2:
        return -1
    return ns


def part_two(input):
    sum = 0
    for j, line in enumerate(input):
        i = 0
        while match := ast_expr.search(line[i:]):
            adjacent = find_n(input, match.start() + i, j)
            if adjacent != -1:
                sum += adjacent[0] * adjacent[1]
            i += match.start() + 1
    return sum


if __name__ == "__main__":
    input = get_input("input.txt")
    print("PartOne", part_one(input))
    print("PartTwo", part_two(input))
