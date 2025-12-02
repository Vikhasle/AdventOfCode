def read_inp():
    fil = open("/home/kre213/Koding/AdventOfCode/2020/7/input",
               "r").read().replace(' bags', '').replace(' bag', '').replace('.', '').split('\n')
    test = [x.split(" contain ") for x in fil]
    return test


def open_bag(bag, bag_table):
    for small_bag in bag_table[bag]:
        if small_bag == "no other":
            return False
        if small_bag == "shiny gold":
            return True
        if open_bag(small_bag, bag_table):
            return True
    return False


def part_one(inp):
    for a in inp:
        a[1] = a[1].split(", ")
        for i, b in enumerate(a[1]):
            a[1][i] = b[2:]
    my_dict = {x[0]: x[1] for x in inp}
    res = 0
    for bag in my_dict:
        if open_bag(bag, my_dict):
            res += 1
    return res


def count_bag(bag, bag_table):
    total = 1
    if bag_table[bag] == 0:
        return total
    for smaller_bag in bag_table[bag]:
        amount = bag_table[bag][smaller_bag]
        total += amount*count_bag(smaller_bag, bag_table)
    return total


def part_two(inp):
    bag_table = {}
    for a in inp:
        if a[1] == 'no other':
            bag_table[a[0]] = 0
        else:
            b = a[1].split(", ")
            bag_table[a[0]] = {x[2:]: int(x[0]) for x in b}
    return count_bag("shiny gold", bag_table)-1
